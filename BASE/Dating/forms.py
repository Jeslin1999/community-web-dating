from django.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Genderselect


class GenderselectForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both'),
    ]
    genderselect = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Genderselect
        fields = ['genderselect']

class LoginForm(AuthenticationForm):
    username = CharField(
        max_length = 15,
        min_length = 4,
        label = 'Username',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )
    
    password = CharField(
        max_length = 15,
        min_length = 4,
        label = 'Pasword',
        required = True,
        widget = PasswordInput({
            'class' : 'form-control'
        })
    )