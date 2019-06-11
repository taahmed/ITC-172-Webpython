from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index' ),
    path('gettracks/', views.gettracks, name='tracks' ),
    path('trackdetail/<int:id>', views.trackdetail, name='details'),
    path('newTracks/', views.newTracks, name='newTracks'), 
    path('recordlabels/', views.recordlables, name='recordlabels'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]