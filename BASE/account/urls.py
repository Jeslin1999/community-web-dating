from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/',user_login,name="login"),
    path('register/',register,name="register"),
    path('registersecond/',registersecond,name="registersecond"),

]