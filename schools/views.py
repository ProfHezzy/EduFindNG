from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SchoolProfile, SchoolMedia, SchoolEvent
from .forms import SchoolProfileForm, SchoolMediaForm, SchoolEventForm

@login_required
def create_school_profile(request):
    if request.method == 'POST':
        form = SchoolProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('school_profile_detail', pk=profile.pk)
    else:
        form = SchoolProfileForm()
    return render(request, 'schools/school_profile_form.html', {'form': form})

@login_required
def edit_school_profile(request, pk):
    profile = get_object_or_404(SchoolProfile, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SchoolProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('school_profile_detail', pk=profile.pk)
    else:
        form = SchoolProfileForm(instance=profile)
    return render(request, 'schools/school_profile_form.html', {'form': form})

def school_profile_detail(request, pk):
    profile = get_object_or_404(SchoolProfile, pk=pk)
    return render(request, 'schools/school_profile_detail.html', {'profile': profile})

@login_required
def add_school_media(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id, user=request.user)
    if request.method == 'POST':
        form = SchoolMediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.school = school
            media.save()
            return redirect('school_profile_detail', pk=school_id)
    else:
        form = SchoolMediaForm()
    return render(request, 'schools/school_media_form.html', {'form': form, 'school': school})

@login_required
def add_school_event(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id, user=request.user)
    if request.method == 'POST':
        form = SchoolEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.school = school
            event.save()
            return redirect('school_profile_detail', pk=school_id)
    else:
        form = SchoolEventForm()
    return render(request, 'schools/school_event_form.html', {'form': form, 'school': school})
