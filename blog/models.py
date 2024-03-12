from django.db import models
from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True


class Transaction(CommonInfo):
    type = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    amount = models.IntegerField()
    

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    account = models.IntegerField()
    phone_number = models.CharField(max_length=11, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Order(CommonInfo):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    discount = models.FloatField()


class Receipt(CommonInfo):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField()
    description = models.CharField(max_length=255)


class Employee(models.Model):
    EMPLOYEE_ROLES = {
        "W": "Worker",
        "ST": "STAFF",
        "SP": "Supervisor",
        "MG": "Manager",
        "AC": "Accountant",
        "MKT": "Marketer"
    }
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    salaray = models.FloatField()
    role = models.CharField(max_length=5, choices=EMPLOYEE_ROLES)
    created = models.DateTimeField(auto_now_add=True)
    

class Board(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    share = models.FloatField()
    account_number = models.CharField(max_length=10)
    account_name = models.CharField(max_length=55)
    bank_name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)


class Company(models.Model):
    balance = models.IntegerField(default=0)


