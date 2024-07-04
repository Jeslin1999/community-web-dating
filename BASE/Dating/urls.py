from django.urls import path
from .views import *

app_name = 'Dating'
urlpatterns = [
  path('',dashboard,name='dashboard')
]