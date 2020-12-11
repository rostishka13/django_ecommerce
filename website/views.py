from django.shortcuts import render
from .models import *

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
	context = {}
	return render(request, 'website/contact.html', context)

def shop(request):
	context = {}
	return render(request, 'website/shop.html', context)

def single(request):
	context = {}
	return render(request, 'website/single.html', context)

def single_shop(request):
	context = {}
	return render(request, 'website/shop-single.html', context)