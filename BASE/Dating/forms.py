from django.forms import ModelForm, TextInput, PasswordInput
from .models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : TextInput({
                'class' : 'form-control'
            }),
             'password' : PasswordInput({
                'class' : 'form-control'
            }),
        }