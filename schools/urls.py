from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_school_profile, name='create_school_profile'),
    path('<int:pk>/edit/', views.edit_school_profile, name='edit_school_profile'),
    path('<int:pk>/', views.school_profile_detail, name='school_profile_detail'),
    path('<int:school_id>/media/add/', views.add_school_media, name='add_school_media'),
    path('<int:school_id>/event/add/', views.add_school_event, name='add_school_event'),
]
