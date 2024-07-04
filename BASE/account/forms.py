from django.forms import *
from django import forms
from .models import User, EmailOTP
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator


# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = EmailOTP
#         fields = ['email']
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
#         }


class OTPForm(forms.Form):
    email = forms.EmailField(required=True)
    otp = forms.CharField(max_length=6, required=True)


class LoginForm(UserCreationForm):
    username = CharField(
        max_length = 15,
        min_length = 4,
        label = 'Username',
        required = True,
        widget = TextInput({
            'class' : 'form-control',
            'placeholder': 'User Name'
        })
    )

    email = EmailField(
        max_length = 50,
        min_length = 3,
        label = 'Email',
        required = True,
        validators= [
            EmailValidator()
        ],
        widget = EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )
    
    password = CharField(
        max_length = 15,
        min_length = 8,
        label = 'Password',
        required = True,
        widget = PasswordInput({
            'class' : 'form-control',
            'placeholder': 'Password'
        })
    )

    def login(self,user):
        user.username = self.cleaned_data['username'],
        user.password = self.cleaned_data['password'],
        user.email = self.cleaned_data['email']
        user.save()

    class Meta:
        model = User
        fields = ('username','password','email')


class RegisterFirstForm(UserCreationForm):
    
    fullname = CharField(
        max_length = 30,
        min_length = 3,
        label = 'Full Nmae',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    dob = DateField(
        label = 'DOB',
        required = True,
        widget = DateInput({
            'class' : 'form-control'
        })
    )

    phone = IntegerField(
        label = 'Phone No:',
        required = True,
        widget = NumberInput({
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

    # class Meta:
    #     model = User
    #     fields = ['first_name','last_name','dob','age','gender']


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

    interest = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Interst',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )
    weight = IntegerField(
        label = 'Weight',
        required = True,
        widget = NumberInput({
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

    qualification = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Qualification',
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    fath = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Faith',
        required = True,
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    community = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Community',
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    mother_tonge = CharField(
        max_length = 15,
        min_length = 1,
        label = 'Mother Tonge',
        widget = TextInput({
            'class' : 'form-control'
        })
    )

    smoking = ChoiceField(
        choices=SMOKE,
        label='Smoking Habbit',  
    )
    drinking = ChoiceField(
        choices= DRINKING,
        label='Drinking ',    
    )
    rel_status = ChoiceField(
        choices= REL_STATAS,
        label='Your Status',  
    )
    image = FileField(
        label="Profile image"

    )
    
    class Meta:
        model = User
        fields = ['dob','phone','gender','interest','qualification','weight','height','rel_status','fath','community','mother_tonge','smoke','drinking','image']
         

# class EmploymentInfoForm(Form):
#     class Meta:
#         model = EmploymentInfo
#         fields = ['user_Id','employment_type','company_name','designation','location','experience_level']


# class RelationshipForm(Form):
#     class Meta:
#         model = Relationship_goal
#         fields = ['user_Id','relationship_type']


# class ProfileImageForm(forms.ModelForm):
#     class Meta:
#         model = ProfileImage
#         fields = ['image']