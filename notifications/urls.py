from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notifications, name='list_notifications'),
    path('read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
]
