from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import send_otp_via_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OTPForm,RegisterFirstForm,LoginForm
# , RegistrationForm, AddressUpsertForm
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView
from .models import EmailOTP,User

# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/Login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password,email=email)    
            if user is not None:
                login(request, user)
                return render(request, 'shared/base.html', {'form': form})
            elif user is None:
                context = {}
                if request.method == 'GET':
                    context['form'] = LoginForm()
                    return render(request, 'account/Login.html', context)
                elif request.method == 'POST':
                    form = LoginForm(data = request.POST)
                    if not form.is_valid():
                        context['form'] = form
                        return render(request, 'account/Login.html', context) 
                    elif form.is_valid():
                        username= request.POST.get('username')
                        password = request.POST.get('password')
                        email = request.POST.get('email')
                        user = User(username=username, password=password, email=email)
                        user = form.save(commit=False)
                        user.set_password(user.password)
                        user.save()
                        email_otp, created = EmailOTP.objects.get_or_create(email=email)
                        email_otp.generate_otp()
                        send_otp_via_email(email_otp.email, email_otp.otp)
                        messages.success(request, 'OTP sent successfully. Please check your email.')
                        return redirect('account:verify_otp')
                else:
                        context['form'] = form
                        return render(request, 'account/login.html', context)
       
        return render(request, 'account/login.html', {'form': form})
    
    
    
# def send_otp(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             email_otp, created = EmailOTP.objects.get_or_create(email=email)
#             email_otp.generate_otp()
#             send_otp_via_email(email_otp.email, email_otp.otp)
#             messages.success(request, 'OTP sent successfully. Please check your email.')
#             return redirect('account:verify_otp')
#     else:
#         form = EmailForm()
#     return render(request, 'account/send_otp.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = form.cleaned_data['otp']
            try:
                email_otp = EmailOTP.objects.get(email=email, otp=otp)
                email_otp.is_verified = True
                email_otp.save()
                messages.success(request, 'OTP verified successfully. You can now log in.')
                return redirect('account:register')
            except EmailOTP.DoesNotExist:
                messages.error(request, 'Invalid email or OTP.')
    else:
        form = OTPForm()
    return render(request, 'account/verify_otp.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('../')


def register(request):
    context = {}
    if request.method == 'GET':
        context['form'] = RegisterFirstForm()
        return render(request, 'account/register.html', context)
    elif request.method == 'POST':
        form = RegisterFirstForm(data = request.POST)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'account/register.html', context) 
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return render(request, 'account/Login.html', context)
    else:
            context['form'] = form
            return render(request, 'account/register.html', context)



# class EmployeeCreateView(LoginRequiredMixin,CreateView):
#     model = EmploymentInfo
#     form_class = EmploymentInfoForm
#     template_name = 'account/employmentinfo.html'

#     def get_queryset(self):
#         return EmploymentInfo.objects.filter(user=self.request.user)
    

# class ProfileView(LoginRequiredMixin, TemplateView):
#     model = User
#     template_name = 'account/view_profile.html'

#     def get_queryset(self):
#         return User.objects.filter(user=self.request.user)
    

# class Relationship(LoginRequiredMixin, TemplateView):
#     model = Relationship_goal
#     template_name = 'account/relationship.html'

#     # def get_queryset(self):
#     #     return User.objects.filter(user=self.request.user)
    

# class ProfileDeleteView(LoginRequiredMixin, View):
#     def get(self, request, id):
#         address = get_object_or_404(User, id=id, user=self.request.user)
#         address.delete()
#         return redirect('account:login')



# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         try:
#             email_otp = EmailOTP.objects.get(email=email, is_verified=True)
#             messages.success(request, 'Login successful.')
#             return redirect('account:index')
#         except EmailOTP.DoesNotExist:
#             messages.error(request, 'Email not verified. Please verify your email first.')
#     return render(request, 'account/Login.html')



     # elif user is None:
            #     context = {}
            #     if request.method == 'GET':
            #         context['form'] = LoginForm()
            #         return render(request, 'account/Login.html', context)
            #     elif request.method == 'POST':
            #         form = LoginForm(data = request.POST)
            #         if not form.is_valid():
            #             context['form'] = form
            #             return render(request, 'account/Login.html', context) 
            #         elif form.is_valid():
            #             username= request.POST.get('username')
            #             password = request.POST.get('password')
            #             email = request.POST.get('email')
            #             user = User(username=username, password=password, email=email)
            #             user = form.save(commit=False)
            #             user.set_password(user.password)
            #             user.save()
            #             email_otp, created = EmailOTP.objects.get_or_create(email=email)
            #             email_otp.generate_otp()
            #             send_otp_via_email(email_otp.email, email_otp.otp)
            #             messages.success(request, 'OTP sent successfully. Please check your email.')
            #             return redirect('account:verify_otp')
                # else:
                #         context['form'] = form
                #         return render(request, 'account/login.html', context)