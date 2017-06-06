from django.contrib import admin

from .models import Channel, ControlMeta, Performer, Sponsor


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ControlMetaAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time')


class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



admin.site.register(Channel, ChannelAdmin)
admin.site.register(ControlMeta, ControlMetaAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Sponsor, SponsorAdmin)
