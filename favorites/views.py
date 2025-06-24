from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorite
from schools.models import SchoolProfile

@login_required
def add_favorite(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id)
    Favorite.objects.get_or_create(user=request.user, school=school)
    return redirect('school_profile_detail', pk=school_id)

@login_required
def remove_favorite(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id)
    Favorite.objects.filter(user=request.user, school=school).delete()
    return redirect('school_profile_detail', pk=school_id)

@login_required
def list_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('school')
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})
