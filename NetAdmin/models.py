from django.db import models
from Account.models import Account
# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    from_ta = models.BooleanField(default=False)
    from_student = models.BooleanField(default=False)
    from_admin = models.BooleanField(default=False)
    from_parents = models.BooleanField(default=False)

    first_message = models.BooleanField(default=True)
    reply_to = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title
