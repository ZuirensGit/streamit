from django.db import models
from django.utils import timezone

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=31)
    main_title = models.TextField()
    main_slogan = models.TextField()
    up_coming_description = models.TextField()

    def __str__(self):
        return self.name

class ControlMeta(models.Model):
    channel = models.ForeignKey('Channel')
    name = models.CharField(max_length=31)
    og_url = models.CharField(max_length=1023, default='http://live.zuirens.com')
    og_title = models.CharField(max_length=31, default='zuirens')
    og_description = models.TextField(blank=True)
    og_image = models.CharField(max_length=1023, default='http://live.zuirens.com')
    performer = models.ForeignKey('performer', null=True, blank=True)
    stream_source = models.CharField(max_length=1023, blank=True)
    background = models.ImageField(upload_to='website_background/', null=True, blank=True)
    viewer_scaler = models.FloatField(default=1.0)
    viewer_offset = models.FloatField(default=0.0)
    viewer_random_range = models.IntegerField(default=0)
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
    background = models.ImageField(upload_to='sponsor_background/')

    def __str__(self):
        return self.name
