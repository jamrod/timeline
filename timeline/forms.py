from django import forms
from .models import Timeline, Time_Capsule

class TimelineForm(models.Model):

    def __str__(self):
        pass

    class Meta:
        model = Timeline
        fields = ('author')

class CapsuleForm(models.Model):

    def __str__(self):
        pass

    class Meta:
        model = Time_Capsule
        managed = ('timeline', 'timestamp', 'contents')