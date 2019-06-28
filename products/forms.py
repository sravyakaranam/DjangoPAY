from django import forms
from products.models import Watch,Phone,Laptop


class LaptopForm(forms.Form):
    name=forms.CharField(label='name')
    cost=forms.IntegerField(label='cost')
    company=forms.CharField(label='company')

class WatchForm(forms.Form):
    name=forms.CharField(label='name')
    cost=forms.IntegerField(label='cost')
    company=forms.CharField(label='company')

class PhoneForm(forms.Form):
    name=forms.CharField(label='name')
    cost=forms.IntegerField(label='cost')
    company=forms.CharField(label='company')

class ProductForm(forms.Form):
    name=forms.CharField(label='name')
    cost=forms.IntegerField(label='cost')
    company=forms.CharField(label='company')
    items=forms.IntegerField(label='items')