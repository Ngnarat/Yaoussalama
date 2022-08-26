from django.shortcuts import render
from contact.models import Contact
from blog.models import BlogPost
from faq.models import FAQ
# Create your views here.


def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/pages/about.html')

def blog(request):
    return render(request,'home/pages/blog.html')

def contact(request):
    contacts = Contact.objects.all()
    return render(request,'home/pages/contact.html',context={"contacts":contacts})

def faq(request):
    articles = FAQ.objects.filter(published = True)
    return render(request,'home/pages/faq.html',context={"articles":articles})


