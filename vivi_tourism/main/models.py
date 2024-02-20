from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Zone(models.Model):

    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)  # Many-to-one relationship with Province

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Villa( models.Model ):
    readonly_fields = ('id',)
    name = models.CharField( max_length=50, null=False )
    kind = models.CharField( max_length=50, null=False )

    explanation_rich = RichTextField(null=True)
    explanation = models.TextField(  )
    is_popular = models.BooleanField(null=True, default=False)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    province = models.ForeignKey(Province, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    type = models.ManyToManyField(Type)  # Many-to-many relationship with Type
    # explanation_rich =
    capacity = models.IntegerField(null=False)
    extra = models.CharField(max_length=1000,null=True)
    num_bathroom = models.IntegerField(null=False)
    default_price = models.IntegerField(null=True, default=1000)
    num_bed = models.IntegerField(null=False)
    num_room = models.IntegerField(null=False)
    avatar = models.ImageField( null=False, )
    address = models.CharField( max_length=300, null=True )
    lat = models.FloatField(null=True )
    long = models.FloatField(null=True )
    has_parking = models.BooleanField(null=True,default=False)
    has_wifi = models.BooleanField(null=True,default=False)
    has_breakfast = models.BooleanField(null=True,default=False)
    has_cleaning_service = models.BooleanField(null=True,default=False)
    has_pool = models.BooleanField(null=True,default=False)
    has_reception = models.BooleanField(null=True,default=False)
    # has_private = models.BooleanField(null=True,default=False)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.zone:
    #         self.province = self.zone.province  # Automatically set province based on the zone
    #     super().save(*args, **kwargs)



class VillaImages( models.Model ):
    readonly_fields = ('id',)

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    image = models.ImageField( null=True, )

    def __str__(self):
        return "Image for:" + self.villa.name



class PriceInterval(models.Model):
    villa = models.ForeignKey( Villa, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):

        return self.villa.name +"__" +str(self.start_date)+"__" + str(self.end_date)

class Reservation(models.Model):

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.IntegerField(null=False)
    name = models.CharField(max_length=70,null=False,default="")
    last_name = models.CharField(max_length=70,null=False,default="")
    address = models.CharField(max_length=150,null=False,default="")
    email = models.EmailField(null=False,unique=False,default="")
    phone = models.CharField(max_length=20,null=False,default="")
    country = models.CharField(max_length=20,default="")
    city = models.CharField(max_length=20,default="")
    zip_code = models.CharField(max_length=6,default="")
    completed = models.BooleanField(null=False,default=False)

    def __str__(self):
        return "Reservation for " + self.villa.name + " " + str(self.start_date) + " - " + str(self.end_date)

class Blog(models.Model):

    title = models.CharField(null=False, max_length=200)
    first_parag_rich = RichTextField(null=True)
    second_parag_rich = RichTextField(null=True)
    third_parag_rich = RichTextField(null=True)
    forth_parag_rich = RichTextField(null=True)
    fifth_parag_rich = RichTextField(null=True)

    first_parag = models.CharField(null=False, max_length=2000)
    second_parag = models.CharField(null=False, max_length=2000)
    third_parag = models.CharField(null=False, max_length=2000)
    forth_parag = models.CharField(null=False, max_length=2000)
    fifth_parag = models.CharField(null=False, max_length=2000)
    display_image = models.ImageField( null=False, )
    first_image = models.ImageField( null=True, )
    second_image = models.ImageField( null=True, )
    third_image = models.ImageField( null=True, )
    mid_title = models.CharField(null=False, max_length=200)
    date = models.DateTimeField( auto_now_add=True )
    def __str__(self):
        return self.title









