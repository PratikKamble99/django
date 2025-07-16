# forms.py
from django import forms
from .models import Product

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'image','in_stock']

class ProductForm(forms.Form):
    name=forms.CharField()
    price=forms.IntegerField()
    image=forms.ImageField()
    in_stock=forms.BooleanField()
