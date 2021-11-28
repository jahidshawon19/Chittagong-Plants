from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import*
from .forms import *
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth.decorators import login_required

################ HOME PAGE VIEW  ##########################
@login_required
def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()

	total_customers = customers.count()
	total_orders = orders.count()

	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()


	myFilter = CustomerFilter(request.GET, queryset=customers)
	customers = myFilter.qs

	context = {'customers':customers, 'orders':orders, 'total_customers':total_customers, 'total_orders':total_orders,'delivered':delivered, 'pending':pending, 'myFilter':myFilter}
	return render(request, 'accounts/dashboard.html', context)



####################CATEGORY VIEWS START#########################	
@login_required
def category(request):
	categories = Category.objects.all()
	totalCat = categories.count()
	myFilter = CategoryFilter(request.GET, queryset=categories)
	categories = myFilter.qs
	context = {'categories':categories,'totalCat':totalCat, 'myFilter':myFilter}
	return render(request, 'accounts/categories.html',context)

@login_required

def createCategory(request):
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('categories')
	context = {'form':form}
	return render(request, 'accounts/create_category.html', context)


@login_required
def updateCategory(request,pk):
	query = Category.objects.get(id=pk)
	form = CategoryUpdateForm(instance=query)
	if request.method == 'POST':
		form = CategoryUpdateForm(request.POST, instance=query)
		if form.is_valid():
			form.save()
			return redirect('categories')
	context = {
		'form':form
	}
	return render(request, 'accounts/create_category.html', context)



@login_required 
def deleteCategory(request,pk):
	query= Category.objects.get(id=pk)
	if request.method == 'POST':
		query.delete()
		return redirect('categories')
	return render(request, 'accounts/delete_category.html')

###############################CATEGORY VIEWS END####################################




##########################PRODUCT VIEWS START##################################
@login_required
def product(request):
	products = Product.objects.all()
	totalProducts = products.count()
	myFilter = ProductFilter(request.GET, queryset=products)
	products = myFilter.qs

	context = {'products':products, 'totalProducts':totalProducts, 'myFilter':myFilter}

	return render(request, 'accounts/products.html',context)

@login_required
def createProduct(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products')
	context = {'form':form}
	return render(request, 'accounts/create_product.html', context)	


@login_required
def updateProduct(request,pk):
	query = Product.objects.get(id=pk)
	form = ProductUpdateForm(instance=query)
	if request.method == 'POST':
		form = ProductUpdateForm(request.POST, instance=query)
		if form.is_valid():
			form.save()
			return redirect('products')
	context = {
		'form':form
	}
	return render(request, 'accounts/create_product.html', context)
@login_required 
def deleteProduct(request,pk):
	query= Product.objects.get(id=pk)
	if request.method == 'POST':
		query.delete()
		return redirect('products')
	return render(request, 'accounts/delete_product.html')


##########################PRODUCT VIEWS END##################################






##############################CUSTOMER VIEWS START################################
@login_required
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	orders_count = orders.count()


	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'orders_count':orders_count, 'myFilter': myFilter}
	return render(request, 'accounts/customer.html', context)

@login_required
def allCustomer(request):
	customer = Customer.objects.all()
	total_customer = customer.count()
	myFilter = CustomerFilter(request.GET, queryset=customer)
	customer = myFilter.qs
	context = {'customer':customer, 'myFilter':myFilter, 'total_customer':total_customer}
	return render(request, 'accounts/all_customer.html', context)
@login_required
def createCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/create_customer.html', context)

@login_required
def updateCustomer(request,pk):
	query = Customer.objects.get(id=pk)
	form = CustomerUpdateForm(instance=query)
	if request.method == 'POST':
		form = CustomerUpdateForm(request.POST, instance=query)
		if form.is_valid():
			form.save()
			return redirect('customers')
	context = {
		'form':form
	}
	return render(request, 'accounts/create_customer.html', context)


@login_required 
def deleteCustomer(request,pk):
	query= Customer.objects.get(id=pk)
	if request.method == 'POST':
		query.delete()
		return redirect('customers')
	return render(request, 'accounts/delete_customer.html')

############################## CUSTOMER VIEWS END ################################










####################################### ORDER VIEWS END #############################
@login_required
def createOrder(request, pk):
	customer = Customer.objects.get(id=pk)
	form = OrderForm(initial={'customer':customer})
	
	if request.method == 'POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form,}
	return render(request, 'accounts/order_form.html', context)
@login_required
def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required
def deleteOrder(request,pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

################################## ORDER VIEWS END ####################################