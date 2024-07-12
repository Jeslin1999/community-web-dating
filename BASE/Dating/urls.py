from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Dating'

urlpatterns = [
    path('selectgender/',GenderselectView.as_view(),name='selectgender'),
    path('login/',LoginView.as_view(),name='login'),
    path('malegrid/',GridviewMale.as_view(),name='malegrid'),
    path('femalegrid/',GridviewFemale.as_view(),name='femalegrid'),
    path('bothgrid/',Gridviewboth.as_view(),name='bothgrid'),
   
]
