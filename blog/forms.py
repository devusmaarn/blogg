from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)