from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm


def user_login(request):
    context = {}
    if request.method == "GET":
        context['form'] = LoginForm()
        return render(request,'Dating/login.html',context)

    elif request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request ,user)
                return HttpResponse("sucess")
            else:
                return HttpResponse("Login faild")
            
        #if the form is not valid
        context['form'] = form
        return render(request,'Dating/login.html',context)
def register(request):
    return render(request,'Dating/register.html')