from allauth.account.forms import SignupForm 
from django import forms
from .models import Address
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class CustomSignupForm(SignupForm): 
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name') 


    def signup(self, request, user): 
        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name'] 
        user.save() 
        return user

class editProfile(forms.Form):
    username = forms.CharField(max_length=30,required=False)
    firstname = forms.CharField(max_length=30,required=False)
    lastname = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=30,required=False)
    phone = forms.CharField(max_length=30,required=False)
    pic = forms.ImageField(required=False)

class trackOrderForm(forms.Form):
    order_ref = forms.CharField(max_length=20)

class EditAddressForm(forms.Form):
    street_address = forms.CharField(max_length=30,required=False)
    address2 = forms.CharField(max_length=30,required=False)
    zipCode = forms.CharField(max_length=30,required=False)
    """ country = CountryField(blank_label='Select Country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100'
    })) """
    city = forms.CharField(max_length=30,required=False)
    default = forms.BooleanField(required=False)