from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Timeline, Time_Capsule
from .forms import TimelineForm, CapsuleForm

def timeline_list(request):
    timeline = Timeline.objects.all()
    return render(request, 'timeline/timeline_list.html', {'timeline': timeline})


def timeline_detail(request, pk):
    timeline = Timeline.objects.get(id=pk)
    return render(request, 'timeline/timeline_detail.html', {'timeline': timeline})


def timeline_create(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            timeline = form.save()
            return redirect('timeline_detail', pk=timeline.id)
    else:
        form = TimelineForm()
    return render(request, 'timeline/timeline_form.html', {'form': form})

@login_required
def timeline_edit(request, pk):
    timeline = Timeline.objects.get(id=pk)
    if request.method == 'POST':
        form = TimelineForm(request.POST, instance=timeline)
        if form.is_valid():
            timeline = form.save()
            return redirect('timeline_detail', pk=timeline.id)
    else:
        form = TimelineForm(instance=timeline)
    return render(request, 'timeline/timeline_form.html', {'form': form})

@login_required
def timeline_delete(request, pk):
    Timeline.objects.get(id=pk).delete()
    return redirect('timeline_list')

# Possible
def capsule_list(request):
    capsule = Time_Capsule.objects.all()
    return render(request, 'timeline/capsule_list.html', {'capsule': capsule})


def capsule_detail(request, pk):
    capsule = Time_Capsule.objects.get(id=pk)
    return render(request, 'timeline/capsule_detail.html', {'capsule': capsule})


# def capsule_create(request, pk):
#     if request.method == 'POST':
#         form = CapsuleForm( request.POST)
#         if form.is_valid():

#             # form.fields['timeline.author'].queryset= Timeline.objects.filter(author = request.user)
#             form.save()                   
#             return redirect('capsule_detail', pk=capsule.id)
#     else:
#         form = CapsuleForm()
#     return render(request, 'timeline/capsule_form.html', {'form': form})


def capsule_create(request):
    # timeline = Timeline.objects.get(id=pk)
    if request.method == 'POST':
        form = CapsuleForm(request.POST)
        if form.is_valid():
            capsule = form.save()
            return redirect('capsule_detail', pk=capsule.id)
    else:
        form = CapsuleForm()
    return render(request, 'timeline/capsule_form.html', {'form': form})




@login_required
def capsule_edit(request, pk):
    capsule = Time_Capsule.objects.get(id=pk)
    if request.method == 'POST':
        form = CapsuleForm(request.POST, instance=capsule)
        if form.is_valid():
            capsule = form.save()
            return redirect('capsule_detail', pk=capsule.id)
    else:
        form = CapsuleForm(instance=capsule)
    return render(request, 'timeline/capsule_form.html', {'form': form})
@login_required

def capsule_delete(request, pk):
    capsule = Time_Capsule.objects.get(id=pk)
    timeline = capsule.timeline
    capsule.delete()
    return redirect('timeline_detail', pk=timeline.id)
