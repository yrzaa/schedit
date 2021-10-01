from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, ManyToManyField

class CustomUser(AbstractUser):
    pass

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class TimeSlot(models.Model):
    startTime = models.DateTimeField(blank=False, null=false)
    endTime = models.DateTimeField(blank=False, null= False)

    certificate = ForeignKey(Certificate, on_delete=models.PROTECT,)
    