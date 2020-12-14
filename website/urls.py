
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('shop/', views.shop, name = 'shop'),
    path('single/<int:pk>/', views.single, name = 'single'),   #blog
    path('single_shop/<int:pk>/', views.single_shop, name = 'single_shop'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('policy/', views.policy, name = 'policy'),
    path('shipping/', views.shipping, name = 'shipping'),
    path('searching_result/', views.searching_result, name = 'searching_result'),


   
]
