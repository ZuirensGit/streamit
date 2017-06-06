from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.utils import timezone

from .models import Channel, ControlMeta, Performer, Sponsor


def channel(request, channel):
    channel = get_object_or_404(Channel, name=channel)
    control_meta = ControlMeta.objects.filter(start_time__gt=timezone.now()).order_by('start_time')[0]
    performers = Performer.objects.filter(start_time__gt=timezone.now()).order_by('start_time')[1:3]
    sponsors = Sponsor.objects.all()
    slider_content_width = 100 / len(sponsors)
    slide_width = 100 * len(sponsors)


    context = {
        'channel': channel,
        'control_meta': control_meta,
        'performers': performers,
        'sponsors': sponsors,
        'slider_content_width': slider_content_width,
        'slide_width': slide_width,
    }

    return render(request, 'index.html', context)
