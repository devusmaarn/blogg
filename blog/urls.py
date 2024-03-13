from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.signout, name='logout'),
    path('dashboard', views.profile),
    
    path('dashboard/customers/', views.CustomerListView.as_view(), name='customers'),
    path('dashboard/customers/new', views.CustomerCreateView.as_view(), name='new_customer'),
    
    path('dashboard/products/', views.ProductListView.as_view(), name='products'),
    path('dashboard/products/new', views.ProductCreateView.as_view(), name='new_product'),
    path('dashboard/products/<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete_product'),
    
    path('dashboard/orders', views.OrderListView.as_view(), name='orders'),
    path('dashboard/orders/new', views.OrderCreateView.as_view(), name='new_order'),
    path('dashboard/orders/<int:pk>/delete', views.OrderDeleteView.as_view(), name='delete_order'),
]