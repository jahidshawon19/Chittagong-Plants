from django.forms import ModelForm
from .models import Order,Customer,Product,Category

class CustomerForm(ModelForm):
	class Meta:
		model = Customer 
		fields = '__all__'

class CustomerUpdateForm(ModelForm):
	class Meta:
		model = Customer 
		fields = '__all__'

class CategoryForm(ModelForm):
	class Meta:
		model=Category 
		fields = '__all__'

class CategoryUpdateForm(ModelForm):
	class Meta:
		model = Category 
		fields = '__all__'

class ProductForm(ModelForm):
	class Meta:
		model = Product 
		fields = '__all__'

class ProductUpdateForm(ModelForm):
	class Meta:
		model = Product 
		fields = '__all__'

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'