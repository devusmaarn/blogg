from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, CustomerForm, ProductForm
from .models import Customer, Product

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
    
    
def register(request):
    return render(request, 'auth.html', {'page': 'register'})


@login_required(login_url='login')
def profile(request):
    return render(request, 'dashboard/index.html')

# Customers
def newCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    form = CustomerForm()
    return render(request, 'dashboard/customer/create.html', {
        "form": form,
    })
    
def customers(request):
    return render(request, 'dashboard/customer/index.html', {
        "customers": Customer.objects.all(),
    })
    
# Products
def newProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    form = ProductForm()
    return render(request, 'dashboard/product/create.html', {
        "form": form,
    })
    
def products(request):
    return render(request, 'dashboard/product/index.html', {
        "products": Product.objects.all(),
    })