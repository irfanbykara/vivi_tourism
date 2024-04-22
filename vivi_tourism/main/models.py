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

class Services(models.Model):
    name = models.CharField(max_length=50)
    explanation = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class CancellationPolicy(models.Model):
    title = models.CharField(max_length=50)
    explanation = models.CharField(max_length=300)

    def __str__(self):
        return self.title + self.explanation



class YatchFeatureCategories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class YatchFeature(models.Model):

    name = models.CharField(max_length=50)
    yatch_feature_categories = models.ForeignKey(YatchFeatureCategories, on_delete=models.CASCADE)  # Many-to-one relationship with Province

    def __str__(self):
        return self.name


class VillaFeatureCategories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class VillaFeature(models.Model):

    name = models.CharField(max_length=50)
    villa_feature_categories = models.ForeignKey(VillaFeatureCategories, on_delete=models.CASCADE)  # Many-to-one relationship with Province
    is_internal = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name




class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TourType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class YatchType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tour(models.Model):

    readonly_fields = ('id',)
    name  = models.CharField( max_length=50, null=False )
    explanation = RichTextField(null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    province = models.ForeignKey(Province, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    default_price = models.IntegerField(null=True, default=1000)
    avatar = models.ImageField( null=False, )
    address = models.CharField( max_length=300, null=True )
    type = models.ManyToManyField(TourType)  # Many-to-many relationship with Type
    tour_duration = models.CharField( max_length=20, null=True )
    has_guide = models.BooleanField(null=True,default=False)
    has_wifi = models.BooleanField(null=True,default=False)
    has_lunch = models.BooleanField(null=True,default=False)
    has_shuttle  = models.BooleanField(null=True,default=False)
    currency = models.CharField( max_length=3, null=True,default="try")

    def __str__(self):
        return self.name


class YatchPort(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Yatch(models.Model):

    readonly_fields = ('id',)
    name = models.CharField( max_length=50, null=False )
    explanation = RichTextField(null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    province = models.ForeignKey(Province, on_delete=models.CASCADE,null=True)  # Many-to-one relationship with Zone
    default_price = models.IntegerField(null=True, default=1000)
    avatar = models.ImageField( null=False, )
    features = models.ManyToManyField(YatchFeature, blank=True)  # Allow blank values
    type = models.ManyToManyField(YatchType, blank=True)  # Many-to-many relationship with Type
    yatch_port = models.ForeignKey(YatchPort, on_delete=models.CASCADE, null=True, blank=True)  # Many-to-one relationship with Zone
    num_bathroom = models.IntegerField(null=False)
    services = models.ManyToManyField(Services, blank=True)  # Allow blank values
    brand = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    model = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    made_year = models.CharField(max_length=4, null=True, blank=True)  # Allow blank values
    renovation_year = models.CharField(max_length=4, null=True, blank=True)  # Allow blank values
    cruising_capacity = models.IntegerField(null=True, blank=True)  # Allow blank values
    capacity = models.IntegerField(null=True, blank=True)  # Allow blank values
    num_rooms = models.IntegerField(null=True, blank=True)  # Allow blank values
    boarding_passanger_capacity = models.IntegerField(null=True, blank=True)  # Allow blank values
    height = models.IntegerField(null=True, blank=True)  # Allow blank values
    cenova = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    main_sail = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    num_engine = models.IntegerField(null=True, blank=True)  # Allow blank values
    engine_type = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    fuel_cost = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    fuel_type = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    yatch_material = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    num_rudder = models.IntegerField(null=True, blank=True)  # Allow blank values
    daily_cruise_duration = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    daily_ac_duration = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    engine_horse_power = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    fuel_capacity = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    waste_tank_capacity = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    water_tank_capacity = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    hall_height = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    width = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    water_draft = models.CharField(max_length=30, null=True, blank=True)  # Allow blank values
    currency = models.CharField(max_length=3, null=True, default="try")


    def __str__(self):
        return self.name

class Villa( models.Model ):

    readonly_fields = ('id',)
    name = models.CharField( max_length=50, null=False )
    kind = models.CharField( max_length=50, null=False )
    explanation_rich = RichTextField(null=True)
    explanation = models.TextField()
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
    cancellation_policy = models.ManyToManyField(CancellationPolicy, blank=True)  # Allow blank values
    features = models.ManyToManyField(VillaFeature, blank=True)  # Allow blank values

    has_parking = models.BooleanField(null=True,default=False)
    has_wifi = models.BooleanField(null=True,default=False)
    has_breakfast = models.BooleanField(null=True,default=False)
    has_cleaning_service = models.BooleanField(null=True,default=False)
    has_pool = models.BooleanField(null=True,default=False)
    has_reception = models.BooleanField(null=True,default=False)
    currency = models.CharField(max_length=3, null=True, default="try")

    # has_private = models.BooleanField(null=True,default=False)

    def __str__(self):
        return self.name



class VillaImages( models.Model ):
    readonly_fields = ('id',)

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    image = models.ImageField( null=True, )

    def __str__(self):
        return "Image for:" + self.villa.name


class TourImages( models.Model ):
    readonly_fields = ('id',)

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField( null=True, )

    def __str__(self):
        return "Tour image for:" + self.tour.name

class YatchImages(models.Model):
    readonly_fields = ('id',)

    yatch = models.ForeignKey(Yatch, on_delete=models.CASCADE)
    image = models.ImageField(null=True, )

    def __str__(self):
        return "Yatch image for:" + self.yatch.name


class PriceInterval(models.Model):
    villa = models.ForeignKey( Villa, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.IntegerField(null=False)
    min_nights = models.IntegerField(null=True)

    def __str__(self):

        return self.villa.name +"__" +str(self.start_date)+"__" + str(self.end_date)

class TourPriceInterval(models.Model):
    tour = models.ForeignKey( Tour, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):

        return self.tour.name +"__" +str(self.start_date)+"__" + str(self.end_date)

class YatchPriceInterval(models.Model):
    yatch = models.ForeignKey( Yatch, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.IntegerField(null=False)
    min_nights = models.IntegerField(null=True)


    def __str__(self):

        return self.yatch.name +"__" +str(self.start_date)+"__" + str(self.end_date)


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



class YatchReservation(models.Model):

    yatch = models.ForeignKey(Yatch, on_delete=models.CASCADE)
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
        return "Reservation for " + self.yatch.name + " " + str(self.start_date) + " - " + str(self.end_date)

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









