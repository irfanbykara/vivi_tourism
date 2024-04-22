from django.contrib import admin
from .models import Villa, VillaImages,PriceInterval,Reservation, \
    Blog,Province,Zone,Type,TourType,Tour,TourPriceInterval,TourImages,\
    YatchFeatureCategories,YatchType,YatchFeature,Yatch,Services,YatchPort,YatchPriceInterval,YatchImages,YatchReservation,\
    CancellationPolicy,VillaFeature,VillaFeatureCategories

# Register your models here.
admin.site.register(Villa)
admin.site.register(VillaImages)
admin.site.register(PriceInterval)
admin.site.register(Reservation)
admin.site.register(Blog)
admin.site.register(Province)
admin.site.register(Zone)
admin.site.register(Type)
admin.site.register(TourType)
admin.site.register(Tour)
admin.site.register(TourPriceInterval)
admin.site.register(TourImages)
admin.site.register(YatchFeature)
admin.site.register(Yatch)
admin.site.register(YatchFeatureCategories)
admin.site.register(YatchType)
admin.site.register(Services)
admin.site.register(YatchPort)
admin.site.register(YatchPriceInterval)
admin.site.register(YatchImages)
admin.site.register(YatchReservation)
admin.site.register(VillaFeature)
admin.site.register(VillaFeatureCategories)
admin.site.register(CancellationPolicy)






