from django import forms

from .models import Customer, Product


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'account']
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'description']