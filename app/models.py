from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class SatImage(models.Model):
    name = models.CharField(max_length=50, blank=True)
    Sat_Main_Img = models.ImageField(upload_to='images/')
    TYPE_SELECT = [
        ('0', 'Roads'),
        ('1', 'Planes'),
        ('2', 'Buildings'),
    ]
    action = models.CharField(max_length=11, choices=TYPE_SELECT , blank=False, default=0)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        related_name='created_by'
    )