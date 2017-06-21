from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.template.defaultfilters import slugify
from django.contrib.staticfiles.templatetags.staticfiles import static


class Channel(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(null=True, blank=True)
    main_title = models.TextField()
    main_slogan = models.TextField()
    up_coming_description = models.TextField()

    def __str__(self):
        return self.name

def create_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(create_slug_pre_save_receiver, sender=Channel)


class ControlMeta(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=31, default='zuirens')
    og_url = models.CharField(max_length=1023, default='http://live.zuirens.com')
    og_title = models.CharField(max_length=100, default='zuirens')
    og_description = models.TextField(blank=True)
    og_image = models.ImageField(upload_to='og_image/', null=True, blank=True, default=static('img/Zuirens-bg.jpg'))
    performer = models.ForeignKey('performer', null=True, blank=True)
    stream_source = models.CharField(max_length=1023, blank=True)
    background = models.ImageField(upload_to='website_background/', null=True, blank=True, default=static('img/Zuirens-bg.jpg'))
    viewer_scaler = models.FloatField(default=1.0)
    viewer_offset = models.FloatField(default=0.0)
    viewer_random_range = models.IntegerField(default=0)
    on_air = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_time',]

# def og_pre_save_receiver(sender, instance, *args, **kwargs):
#     instance.og_title = instance.channel.name
#
# pre_save.connect(og_pre_save_receiver, sender=ControlMeta)


class Performer(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=31)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name',]

class Sponsor(models.Model):
    name = models.TextField()
    description = models.TextField()
    background = models.ImageField(upload_to='sponsor_background/', null=True, blank=True, default=static('img/Zuirens-bg.jpg'))
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Replay(models.Model):
    channel = models.ForeignKey('Channel')
    control_meta = models.ForeignKey('ControlMeta')
    replay_source = models.CharField(max_length=1023, blank=True)
    performer = models.ForeignKey('Performer', null=True, blank=True)
    description = models.TextField(default='zuirens')
    background = models.ImageField(upload_to='replay_background/', null=True, blank=True, default=static('img/Zuirens-bg.jpg'))
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.performer.name

    class Meta:
        ordering = ['-date',]

# def replay_pre_save_receiver(sender, instance, *args, **kwargs):
#     instance.performer = instance.control_meta.performer
#     instance.background = instance.control_meta.background
#     instance.date = instance.control_meta.start_time
#
# pre_save.connect(replay_pre_save_receiver, sender=Replay)
