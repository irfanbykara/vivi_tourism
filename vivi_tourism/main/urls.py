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
    path('yatchs/', views.yatchs, name='yatchs'),

    path('blog/', views.blog, name='blog'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('villa_detail/<int:pk>', views.villa_detail, name='villa_detail'),
    path('tour_detail/<int:pk>', views.tour_detail, name='tour_detail'),
    path('yatch_detail/<int:pk>', views.yatch_detail, name='yatch_detail'),

    path('privacy_agreement/', views.privacy_agreement, name='privacy-agreement'),
    path('cancellation_policy/', views.cancellation_policy, name='cancellation-policy'),

    path('reserve_villa/<int:pk>', views.reserve_villa, name='reserve_villa'),
    path('payment_page/<int:pk>', views.payment_page, name='payment_page'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('sort-villas/', views.sort_villas, name='villa_list'),  # URL pattern for sorting villas
    path('sort-tours/', views.sort_tours, name='sort_tours'),  # URL pattern for sorting villas
    path('sort-yatchs/', views.sort_yatchs, name='sort_yatchs'),  # URL pattern for sorting villas

    path('villa-request/', views.villa_request, name='villa_request'),  # URL pattern for sorting villas
    path('yatch-request/', views.yatch_request, name='yatch_request'),  # URL pattern for sorting villas

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
