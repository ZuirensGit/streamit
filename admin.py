from django.contrib import admin

from .models import Channel, ControlMeta, Performer, Sponsor


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ControlMetaAdmin(admin.ModelAdmin):
    list_editable = ['stream_source', 'on_air']
    list_display = ('name', 'stream_source', 'end_time', 'on_air')

class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



admin.site.register(Channel, ChannelAdmin)
admin.site.register(ControlMeta, ControlMetaAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Sponsor, SponsorAdmin)
