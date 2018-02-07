from django.shortcuts import render
from django.http import  Http404
from .models import Event
# Create your views here.


def index(request):
    all_events = Event.objects.all()
    context = dict(all_events=all_events)

    return render(request, 'index.html', context)
def detail(request, album_id):
    try:
        event = Event.objects.get(pk=album_id)

    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'detail.html', dict(event=event))


    event_id=str(album_id)
    context= dict(all_events=all_events)
    return render(request, 'detail.html', context,event_id)
    #return HttpResponse("<h2> Details for Album id: "+ str(album_id)+"</h2>")
