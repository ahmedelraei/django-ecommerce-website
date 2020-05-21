from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAY_CHOICES = (
    #('S','Card'),
    #('P','Paypal'),
    ('C','Cash'),
    #('F','Fawry'),

)

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'1234 Main ST',
        'class':'form-control'
    }),required=False)
    shipping_address2 = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apartment or suite'
    }))
    shipping_zip = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)

    shipping_country = CountryField(blank_label='Select Country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100'
    }))
    shipping_city = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }),required=False)

    
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)


    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAY_CHOICES) 
