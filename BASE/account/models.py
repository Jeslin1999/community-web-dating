from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # pass 
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
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    intrest = models.CharField(max_length=100,null=True,blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    rel_status = models.CharField(max_length=3, choices=REL_STATAS,default='S')
    fath = models.CharField(max_length=100,null=True,blank=True)
    community = models.CharField(max_length=50,null=True, blank=True)
    mother_tonge = models.CharField(max_length=100,null=True, blank=True)
    smoke = models.CharField(max_length=1,choices=SMOKE,default='N')
    drinking = models.CharField(max_length=1,choices=DRINKING,default='T')
    images = models.FileField(upload_to='upload/',null=True, blank=True)
    video = models.FileField(upload_to='upload/',null=True, blank=True)
