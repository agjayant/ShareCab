from django.db import models

# Create your models here.
class Ride(models.Model):
    destination = models.CharField(max_length=30)
    source =  models.CharField(max_length=30)
    ridetime = models.DateTimeField('leave time')
    capacity = models.IntegerField(default=0)
    def __unicode__(self):
        return self.destination

class Person(models.Model):
    ridegroup = models.ForeignKey(Ride)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
