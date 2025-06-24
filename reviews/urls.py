from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:school_id>/', views.add_review, name='add_review'),
    path('comment/<int:review_id>/', views.add_comment, name='add_comment'),
    path('like/<int:school_id>/', views.like_school, name='like_school'),
    path('unlike/<int:school_id>/', views.unlike_school, name='unlike_school'),
]
