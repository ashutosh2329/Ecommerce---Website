from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('wish_list/', views.wishlist, name="wish_list"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
