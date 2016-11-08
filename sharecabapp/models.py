from django.db import models
from datetime import datetime

# Create your models here.
class Ride(models.Model):
    Auto = 'Au'
    Tempo = 'Te'
    Cab = 'Ca'
    Any = 'An'
    AUTO_TEMPO_CAB_ANY = (
        (Auto, 'Auto'),
        (Tempo, 'Tempo'),
        (Cab, 'Cab'),
        (Any, 'Any'),
    )
    name = models.CharField(max_length=50,default='-')
    destination = models.CharField(max_length=30, default='CNB')
    source =  models.CharField(max_length=30, default='IITK')
    ridetime = models.TimeField('leave time')
    ridedate = models.DateField('leave date')
    preference = models.CharField(max_length=10, choices=AUTO_TEMPO_CAB_ANY, default='Te')
    train = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=254, default='abc@xyz.com')
    def __unicode__(self):
        return self.destination

class Comment(models.Model):
    rideNum = models.ForeignKey(Ride)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    commentTime = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.name

# class Driver(models.Model):
#     userName = models.CharField(max_length=50)
#     vehicleNum = models.ForeignKey(Ride)
#     name = models.CharField(max_length=50)
#     mobile = 
#     commentTime = models.DateTimeField(default=datetime.datetime.now)
#     def __unicode__(self):
#         return self.name
