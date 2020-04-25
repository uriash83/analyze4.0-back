from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse


class Factors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tss = models.CharField(max_length=100)
    atl = models.CharField(max_length=100)
    ctl = models.CharField(max_length=100)
    tbs = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
  

    def __str__(self):
        return self.tss

    
