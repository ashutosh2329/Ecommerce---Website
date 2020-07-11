from django.shortcuts import render, redirect
from .models import *
import json
import datetime

from .forms import CreateUserForm
from django.http import JsonResponse
from .utils import cookieCart,cartData,guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for' + " " + user)
			return redirect('loginpage')


	context = {'form':form}
	return render(request, 'register.html', context)



def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('frontpage')
		else:
			messages.info(request, 'username or password is incorrect')
	context = {}
	return render(request, 'login_Page.html', context)


def logoutUser(request):
	logout(request)
	return redirect('loginpage')

def frontpage(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "frontpage.html", context)

def Bhu_home(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "Bhu_home.html", context)

def Du_home(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "Du_home.html", context)
def Amu_home(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "Amu_home.html", context)

def Th_home(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "Th_home.html", context)



def store(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.filter(category='BHU')
	context = {'products':products,'cartItems':cartItems}
	return render(request, "store.html", context)

def store_Amu(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.filter(category='AMU')
	context = {'products':products,'cartItems':cartItems}
	return render(request, "store_Amu.html", context)

def store_Th(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.filter(category='TH')
	context = {'products':products,'cartItems':cartItems}
	return render(request, "store_Th.html", context)

def store_Du(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.filter(category='DU')
	context = {'products':products,'cartItems':cartItems}
	return render(request, "store_Du.html", context)

def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items,'order':order,'cartItems':cartItems}
	return render(request, "cart.html", context)



def wishlist(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']
	context = {'items':items,'order':order}
	return render(request, "cart.html", context)


def checkout(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items,'order':order,'cartItems':cartItems}
	return render(request, "checkout.html", context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	# print('Action:',action)
	# print('Product:',productId)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, create = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if  orderItem.quantity <= 0:
		orderItem.delete()


	return JsonResponse('item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)


	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == float(order.get_cart_total):
		order.complete = True
	order.save()
	if order.shipping == True:
		ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)
	return JsonResponse('payment submitted..',safe=False)