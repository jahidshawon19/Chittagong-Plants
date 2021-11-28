import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = Order
		fields = '__all__'
		exclude=['customer', 'quantity', 'date_created', 'price','delivery_date']



class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = Product
		fields = '__all__'
		exclude = ['date_created']


class CustomerFilter(django_filters.FilterSet):
	class Meta:
		model = Customer 
		fields = '__all__'
		exclude = ['date_created', 'name', 'address']



class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = Category 
		fields = '__all__'
		exclude = ['date_created']