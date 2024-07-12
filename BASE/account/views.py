from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import EmailForm, LoginForm, RegisterForm, OTPForm, EmployeeForm, JobseekerForm
from django.views.generic import FormView, TemplateView, ListView, CreateView, UpdateView
from .models import User, EmailOTP, Relationship
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from .utils import send_otp_via_email


def index(request):
    return render(request,'account/index.html')

def send_otp(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_otp, created = EmailOTP.objects.get_or_create(email=email)
            email_otp.generate_otp()
            send_otp_via_email(email_otp.email, email_otp.otp)
            return redirect('account:verify_otp')
    else:
        form = EmailForm()
    return render(request, 'account/send_otp.html', {'form': form})

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
                return redirect('account:register')
            except EmailOTP.DoesNotExist:
                messages.error(request, 'Invalid email or OTP.')
    else:
        form = OTPForm()
    return render(request, 'account/verify_otp.html', {'form': form})

        

class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:logina')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.is_email_verified = True
        user.save()
        return redirect('account:logina')
    
    
class RegisterLogin(FormView):
    template_name = 'account/conformup.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None and user.is_email_verified:
                login(self.request, user)
                return redirect('account:employeeinfo')
        else:
            return self.form_invalid(form)

class EmployeeinfoView(LoginRequiredMixin,View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('account:logina')
        employee_form = EmployeeForm()
        jobseeker_form = JobseekerForm()
        return render(request, 'account/employeeinfo.html', {
            'employee_form': employee_form,
            'jobseeker_form': jobseeker_form
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('account:logina')
        if 'employee_submit' in request.POST:
            employee_form = EmployeeForm(request.POST)
            jobseeker_form = JobseekerForm()
            if employee_form.is_valid():
                employee = employee_form.save(commit=False)
                employee.user = request.user
                employee.save()
                return redirect('account:relationship')
        elif 'jobseeker_submit' in request.POST:
            jobseeker_form = JobseekerForm(request.POST)
            employee_form = EmployeeForm()
            if jobseeker_form.is_valid():
                jobseeker = jobseeker_form.save(commit=False)
                jobseeker.user = request.user
                jobseeker.save()
                return redirect('account:relationship')
        return render(request, 'employeeinfo.html', {
            'employee_form': employee_form,
            'jobseeker_form': jobseeker_form
        })
    

class RelationshipView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return render(request, 'account/relationship.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('account:login')
        if 'short_submit' in request.POST:
            short_relationship = Relationship(
                user=request.user,
                relation='short',
            )
            short_relationship.save()
            return redirect('Dating:selectgender') 
        elif 'long_submit' in request.POST:
            pass
        return render(request, 'relationship.html')

        
        
class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Dating:login')
    
        