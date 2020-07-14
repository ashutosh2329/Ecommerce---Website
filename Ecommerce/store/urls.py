from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # user page
    path('registerPage', views.register, name="register"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('logout', views.logoutUser, name="logout"),

    # common urls
    path('', views.frontpage, name="home"),
    path('home', views.store, name="store"),
    path('frontpage/', views.frontpage, name="frontpage"),
    path('store_Th/', views.store_Th, name="store_Th"),
    path('store_Amu/', views.store_Amu, name="store_Amu"),
    path('store_Du/', views.store_Du, name="store_Du"),
    

    # order urls
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),



    # home pages of university
    path('Du_home/', views.Du_home, name="Du_home"),
    path('Bhu_home/', views.Bhu_home, name="Bhu_home"),
    path('Amu_home/', views.Amu_home, name="Amu_home"),
    path('Th_home/', views.Th_home, name="Th_home"),

    #future page
    path('future/',views.future, name="future"),

]
