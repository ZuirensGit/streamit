from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.utils import timezone

from .models import Channel, ControlMeta, Performer, Sponsor


def index(request):
    channel = Channel.objects.all()[0]
    return HttpResponseRedirect('{}/'.format(channel.slug))

def channel(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    control_meta = ControlMeta.objects.filter(on_air=True).order_by('start_time')[0]
    performers = Performer.objects.filter(channel=channel, start_time__gt=timezone.now()).exclude(pk=control_meta.performer.pk).order_by('start_time')[0:3]
    sponsors = Sponsor.objects.all()


    context = {
        'channel': channel,
        'control_meta': control_meta,
        'performers': performers,
        'sponsors': sponsors,
    }

    return render(request, 'index.html', context)
