from django.shortcuts import render, redirect
from .models import Villa,VillaImages,PriceInterval,Reservation,Blog
from django.http import JsonResponse
from datetime import datetime,timedelta
from .utils import *
from json import dumps
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings
# Create your vfiews here.
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib import messages #import messages
import os


def home(request):
    all_villas = Villa.objects.all()
    all_blogs = Blog.objects.all()

    if request.method == "POST":
        data = request.POST
        num_people=data.get("num_people")
        # print(num_people)
        all_villas = all_villas.filter(capacity__gte=int(num_people))
        raw_dates = data.get("datetimes_home")
        raw_dates = raw_dates.split(" - ")
        datetime_check_in,datetime_check_out = raw_date_handler(raw_dates)
        occupying_reservations = Reservation.objects.all()
        occupied_villas = []
        occupied_reservations = []
        delta = timedelta(days=1)
        while datetime_check_in < datetime_check_out:
            occupied_reservations += occupying_reservations.filter(start_date__lte=datetime_check_in, end_date__gt=datetime_check_in)
            datetime_check_in += delta


        villas_to_show = []
        for item in occupied_reservations:
            occupied_villas.append(item.villa)
        for villa in all_villas:
            if villa not in occupied_villas:
                villas_to_show.append(villa)
        print(villas_to_show)

        context = {"villas":villas_to_show}
        return render(request, 'main/villas.html', context )


    context = {"villas":all_villas,"blogs":all_blogs}

    return render(request, 'main/home.html',context)


def blog(request):

    return render( request, 'main/blog.html', )


def about(request):

    return render( request, 'main/about.html', )


def contact(request):
    if request.method == "POST":
        print("Got the post...")

        try:
            if request.method == "POST":
                with get_connection(
                        host=settings.EMAIL_HOST,
                        port=settings.EMAIL_PORT,
                        username=os.environ.get('USER_MAIL'),
                        password=os.environ.get('PASSWORD'),
                        use_tls=settings.EMAIL_USE_TLS,

                ) as connection:
                    subject = request.POST.get("name") + ' '+  request.POST.get("surname")
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST.get("email"), ]
                    message = subject + ' adlı kişiden bir mesajınız var! : ' + request.POST.get("message") + '\n Numara: ' +request.POST.get("phone")
                    EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
            messages.success(request, "Mesajınız başarıyla iletildi.")
            #return redirect('home')

        except:
            messages.error(request, "Mesajınız gönderilemedi. Lütfen tekrar deneyin.")



    return render( request, 'main/contact.html', )


def villas(request):

    all_villas = Villa.objects.all()
    context = {"villas":all_villas}
    return render( request, 'main/villas.html',context )


def villa_detail(request, pk):

    villa = Villa.objects.get( id=pk )
    price_intervals = PriceInterval.objects.all()
    price_intervals = price_intervals.filter(villa=villa)

    if request.method == "POST":
        data = request.POST

        raw_dates = data.get("datetimes").split(" - ")

        datetime_check_in, datetime_check_out = raw_date_handler(raw_dates)

        total_price = get_total_price(datetime_check_in, datetime_check_out, price_intervals, villa)

        reservation = Reservation.objects.create(
            villa=villa,
            start_date=datetime_check_in,
            end_date=datetime_check_out,
            total_price=total_price,
        )
        reservation.save()
        return redirect('reserve_villa', pk=reservation.id)

    reservations = Reservation.objects.filter(villa=villa,completed=True,end_date__gte=datetime.now())

    disabled_days = get_disabled_days(reservations)

    date_list = dumps(disabled_days)

    villa_images = VillaImages.objects.filter(villa=villa)

    context = {'villa': villa,"villa_images":villa_images ,"price_intervals":price_intervals,"date_list":date_list}

    return render(request, 'main/villa_detail.html', context )


def reserve_villa(request, pk):

    reservation = Reservation.objects.get(id=pk)

    if request.method == "POST":
        reservation = Reservation.objects.filter(id=pk)

        data = request.POST
        name = data.get("name")
        last_name = data.get("last_name")
        country = data.get("country")
        city = data.get("city")
        zip = data.get("zip")
        email = data.get("email")
        phone = data.get("phone")
        address = data.get("address")
        reservation.update(
            name = name,
            last_name = last_name,
            country = country,
            city = city,
            zip_code = zip,
            email = email,
            phone = phone,
            address = address
        )

        return redirect("payment_page",pk=pk)

    total_price = reservation.total_price
    reservation_price = total_price / 5

    pay_in_checkin = total_price - reservation_price
    check_in = reservation.start_date
    check_out = reservation.end_date
    villa = reservation.villa
    days = (check_out - check_in).days

    context = {"check_in": check_in, "check_out": check_out, "villa": villa, "days": days, "total_price": total_price,
               "reservation":reservation,
               "reservation_price": reservation_price, "pay_in_checkin": pay_in_checkin,
               }

    return render(request, 'main/reserve_villa.html',context)


def payment_page(request, pk):

    reservation = Reservation.objects.get(id=pk)
    total_price = reservation.total_price
    reservation_price = total_price / 5

    pay_in_checkin = total_price - reservation_price
    check_in = reservation.start_date
    check_out = reservation.end_date
    villa = reservation.villa
    days = (check_out - check_in).days

    context = {"check_in": check_in, "check_out": check_out, "villa": villa, "days": days, "total_price": total_price,
               "reservation":reservation,
               "reservation_price": reservation_price, "pay_in_checkin": pay_in_checkin,
               }
    return render(request, 'main/payment_page.html',context )



def blog_detail(request, pk):

    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.all()
    context = {"blogs":blogs, "blog":blog}
    return render(request, 'main/blog_detail.html', context)

def blog(request):

    blogs = Blog.objects.all()
    context = {"blogs":blogs, }
    return render(request, 'main/blog.html', context)






