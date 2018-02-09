from django.shortcuts import render
from django.http import  Http404
from .models import Event, Gallery
# Create your views here.


def index(request):
    all_events = Event.objects.all().order_by('-id')
    for event in all_events:
        event.event_stage1_artists=event.event_stage1_artists.split(',')
        event.event_stage2_artists=event.event_stage2_artists.split(',')
        event.event_stage3_artists=event.event_stage3_artists.split(',')

    all_galleries=Gallery.objects.all()
    context = dict(all_events=all_events, all_galleries=all_galleries)

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
