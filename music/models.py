from django.db import models


# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    event_logo = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    information = models.CharField(max_length=10000)

    def __str__(self):
        return self.event_title + " - " + self.time + " - " + self.genre
