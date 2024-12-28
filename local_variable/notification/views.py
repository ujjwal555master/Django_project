from django.shortcuts import render
from .models import Notification

def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user, read=False).order_by('-created_at')
    
    if notifications:
        notifications.update(read=True)  # Mark notifications as read when viewed
    
    return render(request, 'notifications/notifications.html', {'notifications': notifications})
