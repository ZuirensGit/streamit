from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from django.http import Http404

from .models import Channel, ControlMeta, Performer, Sponsor


def index(request):
    channel = Channel.objects.all()[0]
    return HttpResponseRedirect('{}/'.format(channel.slug))


def channel(request):
    channel = Channel.objects.all()[0]
    try:
        control_meta = ControlMeta.objects.filter(on_air=True, end_time__gt=timezone.localtime(timezone.now())).order_by('end_time')[0]
    except:
        raise Http404("錯誤")
    performers = Performer.objects.filter(channel=channel, start_time__gt=timezone.localtime(timezone.now())).exclude(pk=control_meta.performer.pk).order_by('start_time')[0:4]
    sponsors = Sponsor.objects.all()


    context = {
        'channel': channel,
        'control_meta': control_meta,
        'performers': performers,
        'sponsors': sponsors,
    }

    return render(request, 'index.html', context)

#
# def channel(request, slug):
#     channel = get_object_or_404(Channel, slug=slug)
#     try:
#         control_meta = ControlMeta.objects.filter(on_air=True, end_time__gt=timezone.localtime(timezone.now())).order_by('end_time')[0]
#     except:
#         raise Http404("錯誤")
#     performers = Performer.objects.filter(channel=channel, start_time__gt=timezone.localtime(timezone.now())).exclude(pk=control_meta.performer.pk).order_by('start_time')[0:4]
#     sponsors = Sponsor.objects.all()
#
#
#     context = {
#         'channel': channel,
#         'control_meta': control_meta,
#         'performers': performers,
#         'sponsors': sponsors,
#     }
#
#     return render(request, 'index.html', context)
