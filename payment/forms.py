from django import forms

class eWalletForm(forms.Form):
    sender_number = forms.CharField(label='Sending Number')
    