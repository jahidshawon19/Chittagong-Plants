from django.db import models

# Create your models here.



class Customer(models.Model):
	name = models.CharField(max_length=50, null=True)
	phone = models.CharField(max_length=20, null=True)
	address = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=50, null=True)
	category = models.ForeignKey(Category,null =True, on_delete=models.SET_NULL)
	price = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for Delivery', 'Out for Delivery'),
			('Delivered', 'Delivered'),
		)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null =True, on_delete=models.SET_NULL)
	quantity = models.CharField(max_length=200, null=True)
	delivery_date = models.DateTimeField(max_length=20, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name

