from django import forms

from .models import Customer, Product, Order


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        

class ProductForm(forms.ModelForm):
    pass
        
        
class OrderForm(forms.Form):
    customer = forms.ChoiceField(choices=Customer.objects.values_list('id', 'name'), required=False)
    product = forms.ChoiceField(choices=Product.objects.values_list('id', 'name'))
    quantity = forms.IntegerField(min_value=1)
    discount = forms.IntegerField()
    supplied = forms.BooleanField(required=False)