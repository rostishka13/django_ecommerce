
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('shop/', views.shop, name = 'shop'),
    path('single/', views.single, name = 'single'),
     path('single_shop/', views.single_shop, name = 'single_shop'),


   
]