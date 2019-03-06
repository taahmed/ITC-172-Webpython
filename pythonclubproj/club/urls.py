from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index' ),
    path('clubresources/', views.clubresources, name='resources' ),
    path('getmeeting/', views.getmeeting, name='getmeetings' ),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),
    path('newresource/', views.newResource, name='newresource'),
  
]