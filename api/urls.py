from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsView.as_view(), name="product"),
    path("products/<int:pk>", views.ProductRetrieveView.as_view(), name="product")
]