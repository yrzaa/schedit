from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey, ManyToManyField

class CustomUser(AbstractUser):
    pass

class Certificate(models.Model):
    '''Model representing a Certificate'''
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    '''Model representing a Timeslot'''
    startTime = models.DateTimeField(blank=False, null=True)
    endTime = models.DateTimeField(blank=False, null= True)

    #certificate = ForeignKey(Certificate, on_delete=models.PROTECT,)

    def __str__(self):
        return f'{self.startTime} to {self.endTime}'

class Application(models.Model):
    '''Model representing a request for a certificate'''
    user = ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, blank= False)

    PROCESSING_STATUS = (
        ('a','Accepted'),
        ('r','Rejected'),
        ('w','Waiting'),
    )
    status= models.CharField(max_length=1,choices=PROCESSING_STATUS, blank=False, default='w')

    collected = models.BooleanField(default=False)
    delayed = models.BooleanField(default=False)

    certificate = ForeignKey(Certificate, on_delete=models.PROTECT, blank=False)
    slot = ForeignKey(TimeSlot ,on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return f'By:{self.user}, For:{self.certificate}, On:{self.slot}, {self.status}, {self.collected}'


