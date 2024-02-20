from django.shortcuts import render, redirect
from .models import Villa,VillaImages,PriceInterval,Reservation,Blog,Zone,Province,Type
from .consts import *
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
import math
from dotenv import load_dotenv
from urllib.parse import unquote
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


load_dotenv()
#

def home(request):

    all_villas = Villa.objects.all().order_by('-is_popular')

    all_blogs = Blog.objects.all()
    all_types = Type.objects.all()

    provinces = Province.objects.all()
    if request.method == "POST":
        data = request.POST
        num_people=data.get("num_people")

        all_villas = all_villas.filter(capacity__gte=int(num_people))
        zone_id = data.get("zone_selection")
        if zone_id:
            if zone_id == "all_zones":
                pass
            else:
                if zone_id.split('_')[1] == "zone":
                    all_villas = all_villas.filter(zone_id=zone_id.split('_')[0])
                else:
                    all_villas = all_villas.filter(province_id=zone_id.split('_')[0])

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
        context_dict = {}
        all_villas = villas_to_show
        # Iterate through each villa to find the minimum price
        # for villa in all_villas:
        #     # Get all price intervals for the current villa
        #     price_intervals = PriceInterval.objects.filter(villa=villa)
        #     if price_intervals.exists():
        #         min_price = min(price_interval.price for price_interval in price_intervals)
        #     else:
        #         min_price = villa.default_price
        for villa in all_villas:
            price_intervals = PriceInterval.objects.filter(villa=villa, start_date__lte=datetime_check_out,
                                                           end_date__gte=datetime_check_in).first()
            if price_intervals!=None:
                min_price = price_intervals.price
            else:
                min_price = villa.default_price
            context_dict[villa] = min_price

            context_dict[villa] = min_price

        context = {"context_dict":context_dict.items(),"provinces":provinces,"all_types":all_types,
                   "raw_dates":raw_dates,"num_people":num_people,"selected_zone_id":zone_id}
        return render(request, 'main/villas.html', context )

    context = {"villas":all_villas,"blogs":all_blogs,"provinces":provinces}

    return render(request, 'main/home.html',context)


def blog(request):

    return render( request, 'main/blog.html', )


def about(request):

    return render( request, 'main/about.html', )


def contact(request):
    if request.method == "POST":

        try:

            if request.method == "POST":

                host = os.environ.get('EMAIL_HOST')
                port = os.environ.get('EMAIL_PORT')
                username = os.environ.get("EMAIL_HOST_USER")
                password = os.environ.get("PASSWORD"),
                use_tls = os.environ.get('EMAIL_USE_TLS')

                with get_connection(
                        host=host,
                        port=port,
                        username=username,
                        password=password[0],
                        use_tls=use_tls,
                ) as connection:

                    subject = request.POST.get("name") + ' ' + request.POST.get("surname")
                    email_from = os.environ.get('EMAIL_HOST_USER')
                    recipient_list = ["erol_songur@hotmail.com",
                                      ]

                    message = subject + ' adlı kişiden bir mesajınız var! :\n email: '+ request.POST.get("email") +"\n"+ request.POST.get("message") + '\n Numara: ' +request.POST.get("phone")
                    EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
            messages.success(request, "Mesajınız başarıyla iletildi.")

        except Exception as e:
            print(e)
            messages.error(request, "Mesajınız gönderilemedi. Lütfen tekrar deneyin.")



    return render( request, 'main/contact.html', )


from django.db.models import Q

def villas(request):

    # Retrieve all villas
    all_villas = Villa.objects.all()
    all_types = Type.objects.all()

    single_type = request.GET.get("type")
    is_default_price = True if request.GET.get("default_price")!=None else False
    if single_type:
        single_type_name = most_searched_dict[single_type]
        all_villas = all_villas.filter(type__name=single_type_name)
    selected_types_encoded = request.GET.getlist('type[]')
    num_people = request.GET.get("num_people") if request.GET.get("num_people")!=None else 1
    selected_zone = request.GET.get("selected_zone")


    all_villas = all_villas.filter(capacity__gte=num_people)
    if selected_zone:
        if selected_zone == "all_zones":
            pass
        else:
            if selected_zone.split('_')[1] == "zone":
                all_villas = all_villas.filter(zone_id=selected_zone.split('_')[0])
            else:
                all_villas = all_villas.filter(province_id=selected_zone.split('_')[0])

    selected_types_decoded = None
    if selected_types_encoded:
        selected_types_decoded = [unquote(type_name) for type_name in selected_types_encoded]


    # Retrieve the query parameter 'type' from the URL
    if selected_types_decoded!=None:
        for type_name in selected_types_decoded:
            all_villas = all_villas.filter(type__name=type_name)


    raw_dates = request.GET.get("datetimes_home")


    if raw_dates!=None:
        raw_dates = raw_dates.split(" - ")

        datetime_check_in, datetime_check_out = raw_date_handler(raw_dates)
        occupying_reservations = Reservation.objects.all()
        occupied_villas = []

        # Iterate over each day within the date range
        current_date = datetime_check_in
        while current_date < datetime_check_out:
            # Filter reservations for the current date
            reservations_on_date = occupying_reservations.filter(start_date__lte=current_date, end_date__gt=current_date)
            # Add the villas from these reservations to the list of occupied villas
            for reservation in reservations_on_date:
                occupied_villas.append(reservation.villa)
            # Move to the next day
            current_date += timedelta(days=1)

        # Filter out occupied villas from all_villas queryset
        all_villas = all_villas.exclude(id__in=[villa.id for villa in occupied_villas])

    # Now you can proceed with the rest of your code without converting all_villas to a list

    provinces = Province.objects.all()
    # Separate popular villas and non-popular villas
    popular_villas = all_villas.filter(is_popular=True)
    non_popular_villas = all_villas.exclude(is_popular=True)

    # Retrieve minimum prices for popular villas
    popular_min_prices = []

    for villa in popular_villas:

        if raw_dates==None:
            min_price = villa.default_price
        else:
            price_intervals = PriceInterval.objects.filter(villa=villa, start_date__lte=datetime_check_out, end_date__gte=datetime_check_in).first()

            if price_intervals!=None:

                min_price = price_intervals.price
            else:
                min_price = villa.default_price
        popular_min_prices.append(min_price)

    # Retrieve minimum prices for non-popular villas
    non_popular_min_prices = []

    for villa in non_popular_villas:
        if raw_dates==None:
            min_price = villa.default_price
        else:
            price_intervals = PriceInterval.objects.filter(villa=villa, start_date__lte=datetime_check_out, end_date__gte=datetime_check_in).first()

            if price_intervals!=None:
                min_price = price_intervals.price
            else:
                min_price = villa.default_price
        non_popular_min_prices.append(min_price)



    # Combine popular and non-popular villas and their minimum prices
    context_dict = {}
    for villa, min_price in zip(popular_villas, popular_min_prices):
        context_dict[villa] = min_price
    for villa, min_price in zip(non_popular_villas, non_popular_min_prices):
        context_dict[villa] = min_price

    # Store the minimum prices in the dictionary
    context = {"context_dict": context_dict.items(),"provinces":provinces,"all_types":all_types,"selected_types":selected_types_decoded,
               "selected_zone_id":selected_zone,"raw_dates":raw_dates}
    return render(request, 'main/villas.html', context)


from datetime import datetime

def villa_detail(request, pk):

    if request.method == "POST":

        villa = Villa.objects.get( id=pk )

        try:
            host = os.environ.get('EMAIL_HOST')
            port = os.environ.get('EMAIL_PORT')
            username = os.environ.get("EMAIL_HOST_USER")
            password = os.environ.get("PASSWORD"),
            use_tls = os.environ.get('EMAIL_USE_TLS')

            with get_connection(
                    host=host,
                    port=port,
                    username=username,
                    password=password[0],
                    use_tls=use_tls,
            ) as connection:

                subject = request.POST.get("name") + ' ' + request.POST.get("surname")
                email_from = os.environ.get('EMAIL_HOST_USER')
                recipient_list = ["erol_songur@hotmail.com",]

                sender_email = request.POST.get("email")
                message = request.POST.get("message")
                phone_number = request.POST.get("tel")
                requested_dates = request.POST.get("datetimes")
                villa_name = villa.name
                message_string = subject + " kişisinden " + requested_dates + " tarih aralığında " + villa_name + " tesisi için bir rezervasyon talebiniz var.\nİletişim Bilgileri:\n" + sender_email + "\n" + phone_number + "\nMesaj:\n" + message
                EmailMessage(subject, message_string, email_from, recipient_list, connection=connection).send()
                print("Email sent.")
                popup_text = villa.name + " adlı tesis için rezervasyon talebiniz iletildi! Ekibimiz en kısa zamanda sizinle iletişime geçecek!"
            messages.success(request, popup_text)
            return redirect('villa_detail', pk=pk)

        except Exception as e:
            print(e)
            messages.error(request, "Mesajınız gönderilemedi. Lütfen tekrar deneyin.")



    villa = Villa.objects.get( id=pk )
    price_intervals = PriceInterval.objects.filter(villa=villa)

    # Get the current date
    current_date = datetime.now().date()
    try:
        price_interval = price_intervals.get(start_date__lte=current_date, end_date__gte=current_date)
        price = price_interval.price
    except PriceInterval.DoesNotExist:
        # Handle the case where there's no price interval for the current date
        # You may want to provide a default price or handle this case differently
        price = villa.default_price

    if request.GET.get("price")!=None:
        price = request.GET.get("price")
    else:
        price = villa.default_price

    # Find the price interval that includes the current date


    reservations = Reservation.objects.filter(villa=villa, completed=True, end_date__gte=datetime.now())
    villa.lat = str(villa.lat).replace(",",".")
    villa.long = str(villa.long).replace(",",".")

    disabled_days = get_disabled_days(reservations)

    date_list = dumps(disabled_days)


    villa_images = VillaImages.objects.filter(villa=villa)

    context = {'villa': villa, "villa_images": villa_images, "price_intervals": price_intervals, "date_list": date_list, "current_price": price}

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

from django.http import JsonResponse
from django.template.loader import render_to_string


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




from django.db.models import Min, F

from django.db.models import Case, When, Value, BooleanField

def sort_villas(request):
    # Extract parameters from the request
    villa_ids = request.GET.getlist('villa_ids')

    villa_ids = villa_ids[0].split(",")
    villa_ids = [int(id) for id in villa_ids]
    prices = request.GET.get('prices')
    prices = [int(price) for price in prices.split(",")]
    # Sort villa_ids and prices based on prices
    sorted_data = sorted(zip(villa_ids, prices), key=lambda x: x[1])

    # Reconstruct dictionary with sorted data
    sorted_dict = {villa_id: price for villa_id, price in sorted_data}
    # Retrieve the villas corresponding to the villa_ids
    villas = Villa.objects.filter(id__in=villa_ids)

    # Annotate each villa with the provided prices
    for index, villa in enumerate(villas):
        villa.price = prices[index]

    # Get the sort option from the request
    sort_option = request.GET.get('sort_option', 'popularity')

    # Define a case expression to prioritize popular villas
    popular_priority = Case(
        When(is_popular=True, then=Value(0)),  # Prioritize popular villas
        default=Value(1),  # Use default value for non-popular villas
        output_field=BooleanField()
    )

    # Sort the villas based on the selected option
    if sort_option == 'popularity':
        villas = villas.order_by(popular_priority)
    elif sort_option == 'price_asc':
        # Sort villas based on prices in ascending order
        sorted_data = sorted(zip(villa_ids, prices), key=lambda x: x[1])
        sorted_dict = {villa_id: price for villa_id, price in sorted_data}
        villas = [Villa.objects.get(id=villa_id) for villa_id in sorted_dict.keys()]
    elif sort_option == 'price_desc':
        # Sort villas based on prices in descending order
        sorted_data = sorted(zip(villa_ids, prices), key=lambda x: x[1], reverse=True)
        sorted_dict = {villa_id: price for villa_id, price in sorted_data}
        villas = [Villa.objects.get(id=villa_id) for villa_id in sorted_dict.keys()]


    # Reconstruct dictionary with sorted data
    sorted_dict = {villa_id: price for villa_id, price in sorted_data}
    # Prepare context dictionary
    context_dict = {}
    for villa in villas:
        context_dict[villa] = sorted_dict.get(villa.id)  # Access price from sorted_dict using villa id

    # Render the template with the sorted villa data
    context = {"context_dict": context_dict.items()}
    html = render_to_string('main/partial_villa_list.html', context)

    # Return the sorted villa data as JSON response
    return JsonResponse({'html': html})

def yatchs(request):

    page_name = "yatch"
    context = {"page_name":page_name}
    return render(request, 'main/coming_soon.html', context )


def tours(request):

    page_name = "tour"
    context = {"page_name":page_name}
    return render(request, 'main/coming_soon.html', context )

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("rememberMe")  # Assuming "rememberMe" is the name of the checkbox

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if remember_me == "on" and user is not None and user.is_active and user.is_superuser:
            # Log the user in and redirect to the admin dashboard
            login(request, user)
            return redirect('admin_dashboard')

        if user is not None and user.is_active and user.is_superuser:
            # Log the user in
            login(request, user)
            # Retrieve all villas (assuming you need this for rendering the admin dashboard)
            villas = Villa.objects.all()
            context = {"villas": villas}
            return render(request, 'main/admin_dashboard.html', context)
        else:
            # Return an error message indicating invalid credentials or inactive superuser
            error_message = "Kullanıcı adı veya şifre hatalı!"
            context = {"error_message": error_message}
            return render(request, 'main/login.html', context)

    # If it's a GET request or authentication fails, just render the login page
    return render(request, 'main/login.html')

def admin_dashboard(request):

    villas = Villa.objects.all()
    context = {"villas":villas}
    if request.POST:
        try:
            villa_id = request.POST.get('villa')
            villa = Villa.objects.get(pk=villa_id)

            # Get the uploaded images
            images = request.FILES.getlist('images')

            # Save each image for the related villa
            for image in images:
                villa_image = VillaImages(villa=villa, image=image)
                villa_image.save()
            messages.success(request, "Görsel ekleme işleme başarıyla gerçekleştirildi!")

            # Optionally, you can redirect the user after saving the images
            return redirect('admin_dashboard')

        except Exception as e :
            print(e)
            messages.warning(request, "Opps, bir hata oluştu. Lütfen tekrar deneyin!")





    return render(request,"main/admin_dashboard.html",context)

def caravans(request):

    page_name = "caravan"
    context = {"page_name":page_name}

    return render(request, 'main/coming_soon.html',context )

import json
def villa_request(request):

    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            selected_date = data.get('value')
            villa_id = data.get('villa_id')
            villa = Villa.objects.get(id=villa_id)
            raw_dates = selected_date.split(" - ")

            datetime_check_in, datetime_check_out = raw_date_handler(raw_dates)

            # Process the selected date
            # Calculate the difference in days
            num_nights = (datetime_check_out - datetime_check_in).days
            # Initialize total price
            total_price = 0

            # Iterate over each day between check-in and check-out dates
            current_date = datetime_check_in
            while current_date < datetime_check_out:
                # Check if there is a price interval for the current day
                price_interval = PriceInterval.objects.filter(
                    villa=villa,
                    start_date__lte=current_date,
                    end_date__gte=current_date
                ).first()

                # If a price interval exists, use its price
                if price_interval:
                    total_price += price_interval.price
                else:
                    # Use the default price of the villa if no price interval exists
                    total_price += villa.default_price

                # Move to the next day
                current_date += timedelta(days=1)

            context = {"num_nights":num_nights,"total_price":total_price}
            html = render_to_string('main/request_summary.html', context)

            return JsonResponse({'html': html})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
