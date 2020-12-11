from django.db import models

# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length = 255, null = False)
	price = models.FloatField()
	information = models.TextField()
	image = models.ImageField(null = True, blank = True)
	#rating

	def __str__(self):
		return self.title