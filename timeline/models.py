from django.db import models


class Timeline(models.Model):
    author = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.author


class Time_Capsule(models.Model):
    timeline = models.ForeignKey(
        Timeline, on_delete=models.CASCADE, related_name='time_capsules')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    contents = models.TextField(default='')

    def __str__(self):
        return self.contents + str(self.created_on)
