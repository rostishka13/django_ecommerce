from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, default='', related_name='customer', related_query_name='customer')
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length = 255, null = False)
	price = models.FloatField()
	information = models.TextField()
	image = models.ImageField(null = True, blank = True)
	#rating

	def __str__(self):
		return self.title


# class Blog(models.Model):
# 	title = models.CharField(max_length = 255, null = False) 
# 	author = models.ForeignKey(User, on_delete = models.CASCADE)
# 	text = models.TextField()
# 	image = models.ImageField(null = True, blank = True)
# 	create_date = models.DateTimeField(default =timezone.now )
# 	published_date = models.DateTimeField(blank = True, null = True)


# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()

# 	def __str__(self):
# 		return self.title




class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
	date_ordered = models.DateTimeField(auto_now_add = True)
	complete = models.BooleanField(default = False)
	transaction_id = models.CharField(max_length = 100, null = True)

	def __str__(self):
		return str(self.id)


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
	quantity = models.IntegerField(default = 0, null = True, blank = True)
	date_added = models.DateTimeField(auto_now_add = True)

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
	address = models.CharField(max_length = 200, null = False)
	city = models.CharField(max_length = 200, null = False)
	state = models.CharField(max_length = 200, null = False)
	zipcode = models.CharField(max_length = 200, null = False)	
	date_added = models.CharField(max_length = 200, null = False)

	def __str__(self):
		return self.address