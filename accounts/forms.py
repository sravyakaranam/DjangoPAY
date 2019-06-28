from django import forms
from accounts.models import Account
from django.contrib.auth.models import User

class CustomForms(forms.Form):
    user=forms.CharField(label='username')
    typeaccount=forms.CharField(label='acctype')
    balance=forms.IntegerField()
    # class Meta:
    #     model=Account
    #     fields='__all__'
class Userform(forms.ModelForm):
    class Meta:
        model =User
        fields=('username','password','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
        }
class SearchForm(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'search','class':'form-control'}))       
    user=forms.CharField(label='username')