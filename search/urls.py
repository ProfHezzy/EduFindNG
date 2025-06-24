from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_schools, name='search_schools'),
    path('compare/', views.compare_schools, name='compare_schools'),
]
