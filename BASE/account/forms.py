from django.forms import ModelForm,Form,NumberInput, IntegerField, TextInput, PasswordInput,CharField,EmailInput,EmailField,DateField,DateInput
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


class RegisterFirstFrom(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','city','dob','age','gender','nationality','intrest','height','rel_status','fath','community','mother_tonge','smoke','drinking','images','video']


class RegisterSecondFrom(ModelForm):
    pass
    # class Meta:
        # model = User
        # fields = ['nationality','intrest','height','rel_status','fath','community','mother_tonge','smoke','drinking','images','video']
         


    # first_name = CharField(
    #     max_length = 15,
    #     min_length = 3,
    #     label = 'First Name',
    #     required = True,
    #     widget = TextInput({
    #         'class' : 'form-control'
    #     })
    # )

    # last_name = CharField(
    #     max_length = 15,
    #     min_length = 1,
    #     label = 'Last Name',
    #     required = True,
    #     widget = TextInput({
    #         'class' : 'form-control'
    #     })
    # )

    # email = EmailField(
    #     max_length = 15,
    #     min_length = 3,
    #     label = 'Email',
    #     required = True,
    #     widget = EmailInput(attrs={
    #         'class': 'form-control'
    #     })
    # )

    # username = CharField(
    #     max_length = 15,
    #     min_length = 4,
    #     label = 'Username',
    #     required = True,
    #     widget = TextInput({
    #         'class' : 'form-control'
    #     })
    # )

    # password = CharField(
    #     label = 'Pasword',
    #     required = True,
    #     widget = PasswordInput({
    #         'class' : 'form-control'
    #     })
    # )

    # dob = DateField(
    #     label = 'DOB',
    #     # required = True,
    #     widget = DateInput({
    #         'class' : 'form-control'
    #     })
    # )

    # age = IntegerField(
    #     label = 'AGE',
    #     required = True,
    #     widget = NumberInput({
    #         'class' : 'form-control'
    #     })
    # )