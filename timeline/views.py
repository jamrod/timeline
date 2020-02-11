from django.shortcuts import render

from .models import Timeline, Time_Capsule

def timeline_list(request):
    timelines = Timeline.objects.all()
    return render(request, 'timeline/timeline_list.html' {'timelines': artist})
