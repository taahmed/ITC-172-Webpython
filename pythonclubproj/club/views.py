from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your views here.
def index(request):
    return render(request, 'club/index.html')
# importing all theobjects under the productstype
def clubmeetings(request):
    meetings_list=Meeting.objects.all()  
    return render (request, 'club/meetings.html',{'meetings_list': meetings_list})

def clubminutes(request):
    minutes_list=MeetingMinutes.objects.all()  
    return render (request, 'club/minutes.html',{'minutes_list': minutes_list})

def clubresources(request):
    resources_list=Resource.objects.all()  
    return render (request, 'club/resources.html',{'resources_list': resources_list})

def clubevents(request):
    events_list=Event.objects.all()  
    return render (request, 'club/events.html',{'events_list': events_list})

