from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('moderate/review/<int:review_id>/', views.moderate_review, name='moderate_review'),
    path('moderate/comment/<int:comment_id>/', views.moderate_comment, name='moderate_comment'),
]
