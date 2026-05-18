from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    meeting_time = models.DateTimeField()
    description = models.TextField()
    users = models.ManyToManyField(User, related_name="events")

    def __str__(self):
        return f"{self.name} — {self.meeting_time:%d.%m %H:%M}"
