from django.db import models
from Account.models import Account

# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    send_time = models.DateTimeField()
    unread = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
