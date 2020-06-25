from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('/home', views.store, name="store"),
    path('frontpage/', views.frontpage, name="frontpage"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
