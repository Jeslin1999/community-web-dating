from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Dating'

urlpatterns = [
    path('selectgender/',GenderselectView.as_view(),name='selectgender'),
    path('login/',LoginView.as_view(),name='login'),
    path('gridview/',Gridview.as_view(),name='gridview'),
    path('locationgridview/',LocationGridview.as_view(),name='locationgridview'),
    path('educationgridview/',EducationGridview.as_view(),name='educationgridview'),
    path('gallery/',GalleryView.as_view(),name='gallery'),
    path('gallery/delete/<int:pk>/', MediaDeleteView.as_view(), name='media-delete'),
    path('all_users/',AllGridview.as_view(),name='all_users'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('send_request/<int:user_id>/', SendrequestView.as_view(), name='send_request'),
    path('accept_requests/', Accepthtmlview.as_view(), name='accept_requests'),
    path('accept_requests/accept_request/<int:request_id>/<str:action>/', AcceptRequestView.as_view(), name='accept_request'),
    path('accept_requests/reject_request/<int:request_id>/', RejectRequestView.as_view(), name='reject_request'),
    path('friends_list/', FriendsListView.as_view(), name='friends_list'),
    path('chat_room//<int:user_id>/', Messageview.as_view(), name='chat_room'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)