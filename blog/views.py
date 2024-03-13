from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views import generic
from django.urls import reverse

from .forms import LoginForm, CustomerForm, ProductForm, OrderForm
from .models import Customer, Product, Order


def index(request):
    return render(request, 'home.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if user:= authenticate(request, **form.cleaned_data):
                login(request, user)
                return redirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
        
    return render(request, 'auth.html', {
        'page': page,
        "form": form
    })
    
def signout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    return render(request, 'dashboard/index.html')

# Customers
class CustomerListView(generic.ListView):
    template_name=  'dashboard/customer/index.html'
    model = Customer
    context_object_name = 'customers'

class CustomerCreateView(generic.CreateView):
    template_name=  'dashboard/customer/create.html'
    model = Customer
    fields = '__all__'
    success_url = '/dashboard/customers/'
    
    
# Products
class ProductListView(generic.ListView):
    template_name = 'dashboard/product/index.html'
    model = Product
    context_object_name = 'products'
    
class ProductCreateView(generic.CreateView):
    template_name=  'dashboard/product/create.html'
    model = Product
    fields = '__all__'
    success_url = '/dashboard/products/'

class ProductDeleteView(generic.DeleteView):
    template_name = 'dashboard/product/delete.html'
    model = Product
    success_url = '/dashboard/products/'
    
    
# Orders
class OrderListView(generic.ListView):
    template_name = 'dashboard/order/index.html'
    model = Order
    context_object_name = 'orders'
    
class OrderCreateView(generic.CreateView):
    template_name=  'dashboard/order/create.html'
    form = OrderForm
    
    def get(self, request):
        return render(request, self.template_name, {
            "form": self.form,
        })
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=form.cleaned_data['product'])
            customer = Customer.objects.get(id=form.cleaned_data['customer']) \
                if form.cleaned_data.get('customer') else None
            quantity = int(form.cleaned_data['quantity'])
            discount = int(form.cleaned_data['discount'])
            total = (product.amount - discount) * quantity
            
            order = Order(
                customer=customer,
                product=product, 
                quantity=quantity, 
                discount=discount, 
                total=total, 
                supplied=form.cleaned_data['supplied']
            )
            order.save()
            return redirect('orders')
        else:
            return render(request, self.template_name, {
                'form': form,
            })

class OrderDeleteView(generic.DeleteView):
    template_name = 'dashboard/order/delete.html'
    model = Order
    success_url = '/dashboard/orders/'