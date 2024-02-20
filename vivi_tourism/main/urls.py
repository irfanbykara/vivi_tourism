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
    path('yatchs/', views.yatchs, name='yatchs'),
    path('caravans/', views.caravans, name='caravans'),
    path('tours/', views.tours, name='tours'),

    path('blog/', views.blog, name='blog'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('villa_detail/<int:pk>', views.villa_detail, name='villa_detail'),
    path('reserve_villa/<int:pk>', views.reserve_villa, name='reserve_villa'),
    path('payment_page/<int:pk>', views.payment_page, name='payment_page'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('sort-villas/', views.sort_villas, name='villa_list'),  # URL pattern for sorting villas
    path('villa-request/', views.villa_request, name='villa_request'),  # URL pattern for sorting villas

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
