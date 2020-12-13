from django.shortcuts import render,get_object_or_404
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
	
	posts = Blog.objects.all()
	context = {'posts': posts}
	return render(request, 'website/blog.html', context)


def contact(request):
	if request.method == "POST":
		name = request.POST['Name']
		email =request.POST['Email']
		phone = request.POST['Phone_number']
		message = request.POST['Message']
		

		#send an email 
		


		send_mail(
			'message from, ' + name, # subject
			message, # message
			email, # from email
			['myemail@gmail.com']
			)
		return render(request, 'website/contact.html', {'name':name, 'email': email, 'phone':phone,'message':message })
	else:
		
		return render(request, 'website/contact.html')

def shop(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'website/shop.html', context)
#single post of blog
def single(request, pk):
	post = get_object_or_404(Blog, pk = pk)
	context = {'post': post}
	return render(request, 'website/single.html', context)
# single product
def single_shop(request,pk):
	product = get_object_or_404(Product, pk = pk)
	context = {'product': product}
	return render(request, 'website/shop-single.html', context)

def gallery(request):
	products = Product.objects.all()
	context = {'products': products}
	
	return render(request, 'website/gallery.html', context)


def policy(request):
	context = {}
	return render(request, 'website/policy.html', context)

def shipping(request):
	context = {}
	return render(request, 'website/shipping.html', context)

