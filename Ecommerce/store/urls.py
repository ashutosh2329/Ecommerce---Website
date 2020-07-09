from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name="home"),
    path('home', views.store, name="store"),
    path('frontpage/', views.frontpage, name="frontpage"),
    path('store_Au/', views.store_Au, name="store_Au"),
    path('store_Amu/', views.store_Amu, name="store_Amu"),
    path('store_Du/', views.store_Du, name="store_Du"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
