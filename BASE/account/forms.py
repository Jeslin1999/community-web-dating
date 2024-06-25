from django.forms import *
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator


User = get_user_model()

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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'age', 'city', 'gender', 'password1', 'password2')


class RegisterFirstForm(UserCreationForm):
    
    first_name = CharField(
        max_length = 15,
        min_length = 3,
        label = 'First Name',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    last_name = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Last Name',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )
    username = CharField(
        max_length = 15,
        min_length = 1,
        label = 'username',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    email = EmailField(
        max_length = 15,
        min_length = 3,
        label = 'Email',
        required = True,
        validators= [
            EmailValidator()
        ],
        widget = EmailInput(attrs={
            'class': 'form-control'
        })
    )

    dob = DateField(
        label = 'DOB',
        # required = True,
        widget = DateInput({
            'class' : 'form-control'
        })
    )

    age = IntegerField(
        label = 'AGE',
        required = True,
        widget = NumberInput({
            'class' : 'form-control'
        })
    )

    city = CharField(
        max_length = 15,
        min_length = 3,
        label = 'City',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]

    gender = ChoiceField(
        choices=GENDER_CHOICES,
        label='Gender',
        required=True,    
    )
    password2 = CharField(
        max_length=15,
        min_length=4,
        label='Password_confirmation',
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )
    password1 = CharField(
        max_length=15,
        min_length=4,
        label='Password',
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )

    # class Meta:
    #     model = User
    #     fields = ['first_name','last_name','email','username','password1','password2','city','dob','age','gender']


# class RegisterSecondFrom(UserCreationForm):
    REL_STATAS = [
        ('S','Single'),
        ('SK','Single with Kid(s)'),
        ('D','Divorced'),
        ('DK','Divorced with Kid(s)'),
        ('W','Widowed'),
        ('WK','Widowed with Kid(s)'),
        ('SP','Separated'),
        ('SPK','Separated with Kid(s)'),
    ]
    SMOKE = [
        ('N','No'),
        ('Y','Yes'),
        ('P','Plan to Quit')
    ]

    DRINKING = [
        ('R','Regular'),
        ('S','Socialy'),
        ('O','Occasionally'),
        ('T','Teetotaler'),
        ('P','Plan to Quit')
    ]
    nationality = CharField(
        max_length = 15,
        min_length = 3,
        label = 'Nationality',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    intrest = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Interst',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    height = IntegerField(
        label = 'Height',
        required = True,
        widget = NumberInput({
            'class' : 'form-control'
        })
    )

    fath = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Fath',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    community = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Community',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    mother_tonge = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Mother Tonge',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    somke = ChoiceField(
        choices=SMOKE,
        label='Smoking Habbit',
        required=True,    
    )
    drinking = ChoiceField(
        choices= DRINKING,
        label='Drinking ',
        required=True,    
    )
    rel_status = ChoiceField(
        choices= REL_STATAS,
        label='Your Status',
        required=True,    
    )
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2','city','dob','age','gender','nationality','intrest','height','rel_status','fath','community','mother_tonge','smoke','drinking','images','video']
         
class EditProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2','city','dob','age','gender','nationality','intrest','height','rel_status','fath','community','mother_tonge','smoke','drinking','images','video']


class UserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2','city','dob','age','gender','nationality','intrest','height','rel_status','fath','community','mother_tonge','smoke','drinking','images','video']
