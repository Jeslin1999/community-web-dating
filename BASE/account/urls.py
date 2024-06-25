from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from .views import RegistrationWizard

app_name = 'account'

urlpatterns = [
    path('',user_login,name="login"),
    path('register/',register,name="register"),
    # path('register/',RegistrationWizard.as_view(),name="register"),
    # path('registersecond/',registersecond,name="registersecond"),
    path('profile/', viewprofile, name='viewprofile'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)