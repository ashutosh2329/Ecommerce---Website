from django.shortcuts import render
from .models import *
import json
import datetime
from django.http import JsonResponse
from .utils import cookieCart,cartData,guestOrder

# Create your views here.

def frontpage(request):
	context={
	    'name':'ashutosh',
	    'page':'frontpage',

	}
	return render(request, "frontpage.html", context)



def store(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.all()
	context = {'products':products,'cartItems':cartItems}
	return render(request, "store.html", context)

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