from django.db import models

# Create your models here.
class Devices(models.Model):
    dev=models.IntegerField(default=0)
    status=models.CharField(max_length=10,default="Off")


class EnergyMeter(models.Model):
    energy=models.IntegerField(default=0)
    volt=models.IntegerField(default=0)
    current=models.FloatField(default=0.0)
    date=models.DateTimeField(auto_now_add=True)