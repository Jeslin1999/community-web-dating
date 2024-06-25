from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterFirstForm,EditProfileForm,UserProfileForm
# ,RegisterSecondFrom
# from formtools.wizard.views import SessionWizardView
from django.contrib.auth import get_user_model


User = get_user_model()

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
    
def logout_view(request):
    logout(request)
    return redirect('../login')
    

def register(request):
    context = {}
    if request.method == "GET":
        context['form'] = RegisterFirstForm()
        return render(request,'account/register.html',context)
    elif request.method == 'POST':
        form = RegisterFirstForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'account/register.html', context)

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return redirect('../login')
        # return render(request, 'account/registersecond.html', context)

def viewprofile(request):
    context = {'user': request.user}
    return render(request, 'account/view_profile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=request.user)
    
    context = {'form': form}
    return render(request, 'account/edit_profile.html', context)











    
# =======================================================================================================================
# FORMS = [("personal_info", RegisterFirstFrom),
#          ("personal_info1", RegisterSecondFrom)]

# TEMPLATES = {"personal_info": "account/register.html",
#              "personal_info1": "account/registersecond.html"}

# class RegistrationWizard(SessionWizardView):
#     form_list = FORMS
#     templates = TEMPLATES

#     def get_template_names(self):
#         return [self.templates[self.steps.current]]

#     def register(self, form_list, **kwargs):
#         form1 = [form.cleaned_data for form in form_list]
#         user = form1.save(commit = False)
#         user.set_password(form1.cleaned_data['password'])
#         user.save()
#         return redirect('../login')
        

# def registersecond(request):
#     context = {}
#     if request.method == "GET":
#         context['form'] = RegisterSecondFrom()
#         return render(request,'account/registersecond.html',context)
#     elif request.method == 'POST':
#         form = RegisterFirstForm(request.POST)
#         if not form.is_valid():
#             context['form'] = form
#             return render(request, 'account/registersecond.html', context)

#         user = form.save(commit=False)
#         user.set_password(user.password)
#         user.save()
#         return redirect('../login')

    # elif request.method == 'POST':
    #     form1 = RegisterSecondFrom(request.POST)
    #     if form1.is_valid():
    #         user = form1.save(commit = False)
    #         user.set_password(form1.cleaned_data['password'])
    #         user.save()
    #         return redirect('../login')
    # else:
    #     form1 = RegisterSecondFrom()
    
    # return render(request, 'account/registersecond.html', {'form': form1})
    
