from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
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
    name = models.CharField(max_length=31)
    og_url = models.CharField(max_length=1023, default='http://live.zuirens.com')
    og_title = models.CharField(max_length=31, default='zuirens')
    og_description = models.TextField(blank=True)
    og_image = models.CharField(max_length=1023, default='http://live.zuirens.com')
    performer = models.ForeignKey('performer', null=True, blank=True)
    stream_source = models.CharField(max_length=1023, blank=True)
    background = models.ImageField(default=static('img/Zuirens-bg.jpg'), upload_to='website_background/', null=True, blank=True)
    viewer_scaler = models.FloatField(default=1.0)
    viewer_offset = models.FloatField(default=0.0)
    viewer_random_range = models.IntegerField(default=0)
    on_air = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_time',]


class Performer(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=31)
    replay_source = models.CharField(max_length=1023, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-start_time',]

class Sponsor(models.Model):
    name = models.CharField(max_length=31)
    description = models.TextField()
    background = models.ImageField(default=static('img/pioneer-dj.jpg'),upload_to='sponsor_background/', null=True, blank=True)

    def __str__(self):
        return self.name
