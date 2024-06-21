from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterFirstFrom
from .models import User


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
    context = {}
    if request.method == 'GET':
        context['form'] = RegisterFirstFrom()
        return render(request,'Dating/register.html',context)
    elif request.method == 'POST':
        form = RegisterFirstFrom(request.POST)
        if form.is_valid():        
            user = form.cleaned_data
            data = User(
                first_name = user['first_name'],
                last_name = user['last_name'],
                email = user['email'],
                username = user['username'],
                password = user['password'],
                dob = user['dob'],
                age = user['age']
                )
            data.save()
            return redirect('../login')
        else:
            form = RegisterFirstFrom()
    
        context['form'] = RegisterFirstFrom()
        return render(request,'Dating/register.html',context)


# def register(request):
#     if request.method == 'POST':
#         form1 = RegisterFirstFrom(request.POST)
#         if form1.is_valid():
#             user = form1.save(commit = False)
#             user.set_password(form1.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form1 = RegisterFirstFrom()
    
#     return render(request, 'Dating/register.html', {'form': form1})
    