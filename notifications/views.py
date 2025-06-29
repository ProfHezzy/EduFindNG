from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def list_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

@login_required
def mark_notification_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications:list')
