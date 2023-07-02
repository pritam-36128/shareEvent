from datetime import date
from django.db import models



class Notification(models.Model):
    eid = models.IntegerField(null=False)
    message = models.CharField(max_length=200)
    date = models.DateField(default=date.today())
    sent = models.BooleanField(default=False)
