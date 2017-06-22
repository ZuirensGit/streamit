from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from django.http import Http404
from datetime import timedelta
import datetime

from .models import Channel, ControlMeta, Performer, Sponsor, Replay


def index(request):
    channel = Channel.objects.all()[0]
    return HttpResponseRedirect('{}/'.format(channel.slug))


def channel(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    try:
        control_meta = ControlMeta.objects.filter(channel=channel, publish=True, end_time__gt=timezone.localtime(timezone.now()) - timedelta(hours=1)).order_by('end_time')[0]
    except:
        control_meta = ControlMeta.objects.filter(channel=channel, publish=True, end_time__lt=timezone.localtime(timezone.now())).order_by('-end_time')[0]
    up_commings = ControlMeta.objects.filter(channel=channel, start_time__gt=timezone.localtime(timezone.now())).exclude(pk=control_meta.pk).order_by('start_time')[0:4]
    sponsors = Sponsor.objects.all()
    replay = Replay.objects.filter(channel=channel).order_by('-date')

    context = {
        'channel': channel,
        'control_meta': control_meta,
        'up_commings': up_commings,
        'sponsors': sponsors,
        'replay': replay,
    }

    return render(request, 'index.html', context)

def replay(request):
    replay = get_object_or_404(Replay, pk=request.GET.get('pk'))

    performer = replay.performer.name
    replay_source = replay.replay_source
    description = replay.description
    background = replay.background.url
    date = replay.date.strftime('%m / %d %Y')

    data = {
        'performer':performer,
        'replay_source':replay_source,
        'description':description,
        'background':background,
        'date':date,
    }

    return JsonResponse(data)
