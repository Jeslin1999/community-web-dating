from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login


def dashboard(request):
    return render(request,'Dating/dashboard.html')