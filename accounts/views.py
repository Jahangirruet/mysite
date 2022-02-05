from django.shortcuts import render
from django.conf import ENVIRONMENT_VARIABLE
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username  = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email  = request.POST['email']

        if password1==password2:
            user =  User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            print("user created")
            #return render(request,'index.html') 
            return redirect('/')            
        else:
            print('password not matching')        
            #return render(request,'signup.html')
    else :    
        return render(request,'signup.html')    
      




def logout(request):
    auth.logout(request)
    return redirect('/')