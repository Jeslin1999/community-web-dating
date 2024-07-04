from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import random
from datetime import date
# Create your models here.



class EmailOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def __str__(self):
        return self.email
    

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
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
    fullname=models.CharField(max_length=25,null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    bio=models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    interest = models.CharField(max_length=100,null=True,blank=True)
    weight = models.FloatField(null=True, blank=True)  
    height = models.PositiveIntegerField(null=True, blank=True)
    qualification=models.CharField(max_length=25,null=True, blank=True)
    rel_status = models.CharField(max_length=3, choices=REL_STATAS,default='S')
    fath = models.CharField(max_length=100,null=True,blank=True)
    community = models.CharField(max_length=50,null=True, blank=True)
    mother_tonge = models.CharField(max_length=100,null=True, blank=True)
    smoke = models.CharField(max_length=1,choices=SMOKE,default='N')
    drinking = models.CharField(max_length=1,choices=DRINKING,default='T')
    images = models.FileField(upload_to='upload/',null=True, blank=True)

    def __str__(self):
        return self.username.username
    
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


class UserMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    additional_image1 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image2 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image3 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image4 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    additional_image5 = models.ImageField(upload_to='additional_images/', blank=True, null=True)
    short_reel = models.FileField(upload_to='short_reels/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Media"