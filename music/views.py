from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.

def index(request):
    all_events = Event.objects.all()
    context= dict(all_events=all_events)
    return render(request, 'index.html', context)
def detail(request, album_id):

    all_events = Event.objects.all()
    context= dict(all_events=all_events)
    return render(request, 'detail.html', context)
    #return HttpResponse("<h2> Details for Album id: "+ str(album_id)+"</h2>")
