# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import MediaType, Tracks, RecordLabels
from .forms import TracksForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'musicapp/index.html')
# importing all theobjects under the productstype
def tracks(request):
    tracks_list=Tracks.objects.all()  
    return render (request, 'musicapp/tracks.html',{'tracks_list': tracks_list})

def gettracks(request):
    tracktitle_list=Tracks.objects.all()  
    return render (request, 'musicapp/tracks.html',{'tracktitle_list': tracktitle_list})

def trackdetail(request, id):
    detail=get_object_or_404(Tracks, pk=id)  
    context={'detail': detail}
    return render (request, 'musicapp/details.html',context= context)

def mediatype(request):
    typename_list=MediaType.objects.all()  
    return render (request, 'musicapp/mediatype.html',{'mediatype_list': mediatype_list})

def recordlables(request):
    recordlables_list=RecordLabels.objects.all()  
    return render (request, 'musicapp/recordlabels.html',{'recordlables_list': recordlables_list})

#form view
@login_required
def newTracks(request):
     form=TracksForm
     if request.method=='POST':
          form=TracksForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TracksForm()
     else:
          form=TracksForm()
     return render(request, 'musicapp/newtrack.html', {'form': form})

def loginmessage(request):
     return render(request, 'musicapp/loginmessage.html')

def logoutmessage(request):
     return render(request, 'musicapp/logoutmessage.html')