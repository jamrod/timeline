from django.db import models
from django.contrib.auth.models import User

class Timeline(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timeline')

    def __str__(self):
        return self.author.username


class Time_Capsule(models.Model):
    timeline = models.ForeignKey(
        Timeline, on_delete=models.CASCADE, related_name='time_capsules')
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    contents = models.TextField(max_length=100, null=True, blank=True)
    image = models.TextField(max_length=100, null=True, blank=True)
    # Youtube videos in the url have watch? but to embed you need /embed/
    video = models.TextField(max_length=100, null=True, blank=True)
    useful_links = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.created_on)
