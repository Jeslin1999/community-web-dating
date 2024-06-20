from django.urls import path
from .views import *

app_name = 'Dating'
urlpatterns = [
    path('login/',user_login,name="login"),
    path('register/',register,name="register"),
]