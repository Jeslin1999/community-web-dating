from django.shortcuts import render
from django.contrib.auth import authenticate,login


def user_login(request):
    return render(request,'Dating/login.html')

def register(request):
    return render(request,'Dating/register.html')