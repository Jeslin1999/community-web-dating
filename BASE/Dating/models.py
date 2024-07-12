from django.db import models
from account.models import User

# Create your models here.


GENDERSELECT=[
    ('B','Both'),
    ('M','Male'),
    ('F','Female')
]
class Genderselect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genderselect = models.CharField(max_length=1,choices=GENDERSELECT,default='B')

    def __str__(self):
        return f"{self.genderselect}"
