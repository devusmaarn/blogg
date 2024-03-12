from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.signout, name='logout'),
    path('dashboard', views.profile),
    path('dashboard/customers', views.customers, name='customers'),
    path('dashboard/customers/new', views.newCustomer, name='new_customer'),
    path('dashboard/products', views.products, name='products'),
    path('dashboard/products/new', views.newProduct, name='new_product'),
]