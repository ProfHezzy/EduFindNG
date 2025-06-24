from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:school_id>/', views.add_favorite, name='add_favorite'),
    path('remove/<int:school_id>/', views.remove_favorite, name='remove_favorite'),
    path('list/', views.list_favorites, name='list_favorites'),
]
