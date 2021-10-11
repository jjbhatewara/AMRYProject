from django.db import models

# Create your models here.


class SatImage(models.Model):
    name = models.CharField(max_length=50, blank=True)
    Sat_Main_Img = models.ImageField(upload_to='images/')
    TYPE_SELECT = [
        ('0', 'Roads'),
        ('1', 'Planes'),
    ]
    action = models.CharField(max_length=11, choices=TYPE_SELECT , blank=False, default=0)
