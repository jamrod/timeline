from django import forms
from .models import Timeline, Time_Capsule

class TimelineForm(forms.ModelForm):

    def __str__(self):
        pass

    class Meta:
        model = Timeline
        fields = ('author',)

class CapsuleForm(forms.ModelForm):

    def __str__(self):
        pass

    class Meta:
        model = Time_Capsule
        fields = ('timeline', 'timestamp', 'contents',)