from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import GenderselectForm, LoginForm
from django.views.generic import FormView, TemplateView, ListView, CreateView, UpdateView
from .models import Genderselect
from account.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class GenderselectView(LoginRequiredMixin, FormView):
    template_name = 'Dating/selectgender.html'
    form_class = GenderselectForm
    success_url = reverse_lazy('account:logout')
    def form_valid(self, form):
        genderselect, created = Genderselect.objects.update_or_create(
            user=self.request.user,
            defaults={'genderselect': form.cleaned_data['genderselect']}
        )
        return super().form_valid(form)
    

class LoginView(FormView):
    template_name = 'account/Login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            gender_selection = Genderselect.objects.filter(user=user).first()
            if gender_selection:
                login(self.request, user)
                if gender_selection.genderselect == 'B':
                    return redirect('Dating:bothgrid')
                elif gender_selection.genderselect == 'M':
                    return redirect('Dating:malegrid')
                elif gender_selection.genderselect == 'F':
                    return redirect('Dating:femalegrid')
        else:
            return self.form_invalid(form) 

        return super().form_valid(form)
    
    
class GridviewMale(LoginRequiredMixin,ListView):
    model = User
    template_name = 'Dating/malegrid.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(gender='M').exclude(id=self.request.user.id)

class GridviewFemale(LoginRequiredMixin,ListView):
    model = User
    template_name = 'Dating/femalegrid.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(gender='F').exclude(id=self.request.user.id)


class Gridviewboth(LoginRequiredMixin,ListView):
    model = User
    template_name = 'Dating/bothgrid.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().exclude(id=self.request.user.id)
