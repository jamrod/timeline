from django import forms
from .models import Timeline, Time_Capsule

class TimelineForm(forms.ModelForm):

    def __str__(self):
        pass

    class Meta:
        model = Timeline
        fields = ('author',)

class CapsuleForm(forms.ModelForm):
    

    class Meta:
        model = Time_Capsule
        # exclude = ('timeline',)
        # fields = ( 'contents','image', 'video', 'useful_links',)
        fields = ( 'timeline', 'contents','image', 'video', 'useful_links',)
