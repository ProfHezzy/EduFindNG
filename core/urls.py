# core/urls.py
from django.urls import path
from . import views

app_name = 'core' # IMPORTANT: Define an app_name for namespacing

urlpatterns = [
    path('', views.home_view, name='home'), # Your homepage view
    # path('about/', views.about_view, name='about'),
    # ... other core-specific URLs
]