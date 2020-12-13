from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length = 255, null = False)
	price = models.FloatField()
	information = models.TextField()
	image = models.ImageField(null = True, blank = True)
	#rating

	def __str__(self):
		return self.title


class Blog(models.Model):
	title = models.CharField(max_length = 255, null = False) 
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	text = models.TextField()
	image = models.ImageField(null = True, blank = True)
	create_date = models.DateTimeField(default =timezone.now )
	published_date = models.DateTimeField(blank = True, null = True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



