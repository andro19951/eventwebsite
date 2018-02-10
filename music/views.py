from django.shortcuts import render
from django.http import  Http404
from .models import Event, Gallery

from django.core.mail import send_mail


def sendmail():

    send_mail(
        'Subject here',
        'Here is the message.',
        'me@example.com',
        ['andro19951@gmail.com']
    )

def parser(event):
    if event.event_stage1_name=="Null":
        event.event_stage1_name=None
        event.event_stage1_artists=None
    else:
        event.event_stage1_name = event.event_stage1_name.split('.,!')
        event.event_stage1_artists = event.event_stage1_artists.split(',')
    if event.event_stage2_name=="Null":
        event.event_stage2_name=None
        event.event_stage2_artists=None
    else:
        event.event_stage2_name = event.event_stage2_name.split('.,!')
        event.event_stage2_artists = event.event_stage2_artists.split(',')
    if event.event_stage3_name=="Null":
        event.event_stage3_name=None
        event.event_stage3_artists=None
    else:
        event.event_stage3_name=event.event_stage3_name.split('.,!')
        event.event_stage3_artists = event.event_stage3_artists.split(',')

    return event

def index(request):
    all_events = Event.objects.all().order_by('-id')
    for event in all_events:
        event=parser(event)
    if(request.GET.get('Sendbtn')):
        sendmail()

    all_galleries=Gallery.objects.all()
    context = dict(all_events=all_events, all_galleries=all_galleries)

    return render(request, 'index.html', context)
def detail(request, album_id):

    try:
        event = Event.objects.get(pk=album_id)


    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    event=parser(event)
    return render(request, 'detail.html', dict(event=event))


    event_id=str(album_id)
    context= dict(all_events=all_events)
    return render(request, 'detail.html', context,event_id)
    #return HttpResponse("<h2> Details for Album id: "+ str(album_id)+"</h2>")
