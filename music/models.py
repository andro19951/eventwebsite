from django.db import models
from CoolApp1 import settings

# Create your models here.


class Event(models.Model):

    event_title = models.CharField(max_length=250)
    event_artist = models.CharField(max_length=250)
    event_logo = models.CharField(max_length=1000)
    event_fbPage = models.CharField(max_length=250)
    time = models.DateField("Event Date:")
    event_tkPrice = models.DecimalField(max_digits = 4, decimal_places = 2)
    information = models.CharField(max_length=10000)

    def __str__(self):
        return self.event_title + " - " + self.event_artist
