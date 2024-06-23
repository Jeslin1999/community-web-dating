from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterFirstFrom
from .models import User


def user_login(request):
    context = {}
    if request.method == "GET":
        context['form'] = LoginForm()
        return render(request,'account/login.html',context)

    elif request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request ,user)
                return render(request,'account/base.html',context)
            else:
                return HttpResponse("Login faild")
            
        #if the form is not valid
        context['form'] = form
        return render(request,'account/login.html',context)
    

def register(request):
    if request.method == 'POST':
        form1 = RegisterFirstFrom(request.POST)
        if form1.is_valid():
            user = form1.save(commit = False)
            user.set_password(form1.cleaned_data['password'])
            user.save()
            return redirect('../login')
    else:
        form1 = RegisterFirstFrom()
    
    return render(request, 'account/register.html', {'form': form1})
    