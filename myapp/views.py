from django.shortcuts import render
from .models import ProductDetails
from django.conf import ENVIRONMENT_VARIABLE
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def product_list(request):
   
    prds = ProductDetails.objects.all()
    
    return render(request,'product-list.html',{'prds': prds})


def product_detail(request):
    prdtls = ProductDetails.objects.all()
    return render(request,'product-detail.html',{'prdtls':prdtls})


def wishlist(request):
    return render(request,'wishlist.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        usernmame  = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email  = request.POST['email']

        if password1==password2:
            user = User.objects.create_user(usernmame=usernmame,password=password1,first_name=first_name,last_name=last_name,email=email)
            user.save();
            print("user created")
            return render(request,'signup.html')
        else:
            print('password not matching')        
            return redirect('/')
    else :    
       return render(request, 'signup.html')

def MyAccount(request):
    return render(request, 'my-account.html')