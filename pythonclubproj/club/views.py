from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import ResourceForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')
# importing all theobjects under the productstype
def clubresources(request):
    resources_list=Resource.objects.all()  
    return render (request, 'club/resources.html',{'resources_list': resources_list})

def getmeeting(request):
    meetings_list=Meeting.objects.all()  
    return render (request, 'club/meetings.html',{'meetings_list': meetings_list})

def meetingdetail(request, id):
    detail=get_object_or_404(Meeting, pk=id)  
    context={'detail': detail}
    return render (request, 'club/details.html',context= context)

def clubminutes(request):
    minutes_list=MeetingMinutes.objects.all()  
    return render (request, 'club/minutes.html',{'minutes_list': minutes_list})

def clubevents(request):
    events_list=Event.objects.all()  
    return render (request, 'club/events.html',{'events_list': events_list})

#form view

def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'club/newresource.html', {'form': form})

