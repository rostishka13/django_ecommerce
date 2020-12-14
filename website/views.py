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
	special_offers = Product.objects.filter(price__lte = 10)
	products = Product.objects.all()
	context = {'products':products, 'special_offers':special_offers}
	return render(request, 'website/shop.html', context)
#single post of blog
def single(request, pk):
	post = get_object_or_404(Blog, pk = pk)
	context = {'post': post}
	return render(request, 'website/single.html', context)
# single product
def single_shop(request,pk):
	feature_offers = Product.objects.filter(price__gte = 14)
	special_offers = Product.objects.filter(price__lte = 10)
	product = get_object_or_404(Product, pk = pk)
	context = {'product': product,'special_offers':special_offers,'feature_offers':feature_offers}
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

def searching_result(request):
	special_offers = Product.objects.filter(price__lte = 10)
	qs = Product.objects.all()
	query = request.GET.get('search')
	if query != '' and query is not None:
		qs = qs.filter(title__icontains = query) 
	context = {"products": qs,'special_offers':special_offers}
	return render(request, 'website/search_bar.html', context)


