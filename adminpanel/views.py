from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from schools.models import SchoolProfile
from reviews.models import Review, Comment
from accounts.models import User

@staff_member_required
def admin_dashboard(request):
    schools = SchoolProfile.objects.all()
    users = User.objects.all()
    reviews = Review.objects.all()
    comments = Comment.objects.all()
    return render(request, 'adminpanel/dashboard.html', {
        'schools': schools,
        'users': users,
        'reviews': reviews,
        'comments': comments,
    })

@staff_member_required
def moderate_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    review.approved = not review.approved
    review.save()
    return redirect('adminpanel:dashboard')

@staff_member_required
def moderate_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.approved = not comment.approved
    comment.save()
    return redirect('adminpanel:dashboard')
