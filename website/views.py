from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.
def home(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'website/home.html',context)

def about(request):
	context = {}
	return render(request, 'website/about.html', context)


def blog(request):
	context = {}
	return render(request, 'website/blog.html', context)


def contact(request):
	if request.method == "POST":
		name = request.POST['Name']
		email =request.POST['Email']
		phone = request.POST['Phone_number']
		message = request.POST['Message']
		return render(request, 'website/contact.html', {'name':name, 'email': email, 'phone':phone,'message':message })

		#send an email 
		send_mail(
			'message from, ' + name, # subject
			message, # message
			email, # from email
			['rostishka1@gmail.com', 'rostyslav.tykhovski@gmail.com'], # to email

			)

	else:
		
		return render(request, 'website/contact.html')

def shop(request):
	context = {}
	return render(request, 'website/shop.html', context)

def single(request):
	context = {}
	return render(request, 'website/single.html', context)

def single_shop(request):
	context = {}
	return render(request, 'website/shop-single.html', context)