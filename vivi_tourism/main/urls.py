from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('villas/', views.villas, name='villas'),
    path('blog/', views.blog, name='blog'),

    path('villa_detail/<int:pk>', views.villa_detail, name='villa_detail'),
    path('reserve_villa/<int:pk>', views.reserve_villa, name='reserve_villa'),
    path('payment_page/<int:pk>', views.payment_page, name='payment_page'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
