from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
            subject = "Reply:Dex Softwares Client Department"
            message = "Hello,this is Rohan from Dex.\nThank You for chosing us.Our representative shall get back to you. It shall be great to talk business.\n" \
                      "For further queries contact:\n" \
                      "9654827013"
            from_email = settings.EMAIL_HOST
            to_list = [subscriptionForm.data.__getitem__('email')]
            send_mail(subject, message, from_email, to_list)
            return HttpResponseRedirect('/success/')
        elif (subscriptionForm.is_valid()):
            print("valid")
            subscriptionForm.save(commit=True)
            subject="Subscription Started!!"
            message="Hello,this is Rohan from Dex.\nThank You for connecting with us.We assure that this relationship shall grow stronger with each coming day! See you soon."
            from_email = settings.EMAIL_HOST
            to_list=[subscriptionForm.data.__getitem__('email')]
            send_mail(subject,message,from_email,to_list)
            return HttpResponseRedirect('/success/')
        else:
            print("FORM_INVALID")
    return render(request,'home/index.html',{'subscriber_form':subscriptionForm,'contact_form':contactForm,})


def response_received(request):
    return render(request,'home/thankyou.html')

