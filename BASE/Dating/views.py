from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterFirstFrom


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
    

# def register(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = RegisterFirstFrom()
#         return render(request,'Dating/register.html',context)
#     elif request.method == 'POST':
#         form = RegisterFirstFrom(request.POST)
#         if form.is_valid():        
#             user = form.save(commit=False)
#             user.set_password(user.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#         else:
#             # return render(request,'Dating/register.html')
#             context['form'] = RegisterFirstFrom()
#             return render(request,'Dating/register.html',context)


def register(request):
    if request.method == 'POST':
        form = RegisterFirstFrom(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterFirstFrom()
    
    return render(request, 'Dating/register.html', {'form': form})
    