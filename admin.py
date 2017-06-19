from django.contrib import admin

from .models import Channel, ControlMeta, Performer, Sponsor, Replay


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ControlMetaAdmin(admin.ModelAdmin):
    list_editable = ['stream_source' ,'publish' ,'on_air']
    list_display = ('name', 'performer', 'stream_source', 'start_time', 'end_time', 'publish', 'on_air', )

class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ReplayAdmin(admin.ModelAdmin):
    list_display = ('performer', 'date')



admin.site.register(Channel, ChannelAdmin)
admin.site.register(ControlMeta, ControlMetaAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Replay, ReplayAdmin)
