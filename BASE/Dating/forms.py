from django.forms import ModelForm,Form, TextInput, PasswordInput,CharField
from .models import User

class LoginForm(Form):
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