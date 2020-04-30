from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAY_CHOICES = (
    ('S','Card'),
    ('P','Paypal'),
    ('C','Cash'),
    ('F','Fawry'),

)

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'1234 Main ST',
        'class':'form-control'
    }))
    suite   = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apartment or suite'
    }))
    zipCode = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    saveInfo = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAY_CHOICES) 
