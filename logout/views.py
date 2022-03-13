from django.shortcuts import render
from django.shortcuts import render
from django.conf import ENVIRONMENT_VARIABLE
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


