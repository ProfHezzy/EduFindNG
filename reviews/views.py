from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Comment, Like
from .forms import ReviewForm, CommentForm
from schools.models import SchoolProfile

@login_required
def add_review(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.school = school
            review.save()
            return redirect('school_profile_detail', pk=school_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'school': school})

@login_required
def add_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('school_profile_detail', pk=review.school.pk)
    else:
        form = CommentForm()
    return render(request, 'reviews/comment_form.html', {'form': form, 'review': review})

@login_required
def like_school(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id)
    Like.objects.get_or_create(user=request.user, school=school)
    return redirect('school_profile_detail', pk=school_id)

@login_required
def unlike_school(request, school_id):
    school = get_object_or_404(SchoolProfile, pk=school_id)
    Like.objects.filter(user=request.user, school=school).delete()
    return redirect('school_profile_detail', pk=school_id)
