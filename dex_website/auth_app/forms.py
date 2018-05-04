from django import forms
from .models import contactData,UpdateSubscribe
class contactForm(forms.ModelForm):
    class Meta():
        model=contactData
        fields='__all__'
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control','style':'margin-bottom:15px;background-color:rgba(255,255,255,0.8)'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control','style':'margin-bottom:15px;background-color:rgba(255,255,255,0.8)'}),
            'email' : forms.TextInput(attrs={'class': 'form-control','style':'margin-bottom:15px;background-color:rgba(255,255,255,0.8)'}),
            'company' : forms.TextInput(attrs={'class': 'form-control','style':'margin-bottom:15px;background-color:rgba(255,255,255,0.8)'})
        }

class subscribeForm(forms.ModelForm):
    class Meta():
        model=UpdateSubscribe
        fields='__all__'
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'margin-bottom:15px;','placeholder':'Enter your email Id'}),
        }
