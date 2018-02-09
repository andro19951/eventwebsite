from django.db import models
# Create your models here.


class Event(models.Model):
    def default_metki():
        return "None"


    event_title = models.CharField(max_length=250)
    event_logo = models.CharField(max_length=1000)
    event_fbPage = models.CharField(max_length=250)
    time = models.DateField("Event Date:")
    event_tkPrice = models.DecimalField(max_digits=4, decimal_places=2)
    information = models.TextField(max_length=100000)
    event_stage1_name=models.CharField(max_length=250)
    event_stage1_artists = models.CharField(max_length=350)
    event_stage2_name = models.CharField(max_length=250, default = default_metki)
    event_stage2_artists = models.CharField(max_length=350, default = default_metki)
    event_stage3_name = models.CharField(max_length=250, default = default_metki)
    event_stage3_artists = models.CharField(max_length=350, default = default_metki)


    def __str__(self):
        return self.event_title + " - " + str(self.time)


class Gallery(models.Model):
    picture = models.ImageField(upload_to='music/static/assets/css/images')

    def __str__(self):
        return "traki"