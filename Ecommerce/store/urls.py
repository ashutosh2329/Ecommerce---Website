from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name="home"),
    path('home', views.store, name="store"),
    path('frontpage/', views.frontpage, name="frontpage"),
    path('Bhu_home/', views.Bhu_home, name="Bhu_home"),
    path('store_Th/', views.store_Th, name="store_Th"),
    path('store_Amu/', views.store_Amu, name="store_Amu"),
    path('store_Du/', views.store_Du, name="store_Du"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
