from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    contactForm=forms.contactForm()
    subscriptionForm = forms.subscribeForm()

    if request.method=='POST':
        contactForm=forms.contactForm(request.POST)
        subscriptionForm=forms.subscribeForm(request.POST)

        if(contactForm.is_valid()):
            contactForm.save(commit=True)
            return HttpResponseRedirect('/success/')
        elif (subscriptionForm.is_valid()):
            subscriptionForm.save(commit=True)
            return HttpResponseRedirect('/success/')
        else:
            print("FORM_INVALID")
    return render(request,'home/index.html',{'subscriber_form':subscriptionForm,'contact_form':contactForm,})


def response_received(request):
    return render(request,'home/thankyou.html')

