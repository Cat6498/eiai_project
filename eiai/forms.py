from django import forms 
from django.contrib.auth.models import User
from eiai.models import UserProfile, Address 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class AddressForm(forms.ModelForm): 
    
    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'zip_code', 'country')

