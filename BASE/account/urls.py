from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'

urlpatterns = [
    # path('', send_otp, name='send_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('', LoginView.as_view(), name='login'),
    path('register/',register,name='register'),
    path('logout/', logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)