from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import NotificationsForm
from .models import Notifications
# Create your views here.

def create_notification(request):
    if request.method == 'POST':
        form = NotificationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationsForm()
    return render(request, 'notifications/create_notification.html', {'form': form})


def notification_list(request):
    notifications = Notifications.objects.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})


def edit_notification(request, id):
    notification = Notifications.objects.get(id=id)
    if request.method == "POST":
        form = NotificationsForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
        return redirect('notification_detail_view', id=id)
    else:
        form = NotificationsForm(instance=notification)
    return render(request, "notifications/edit_notification.html", {"form": form})



def notification_details(request, id):
    notification = Notifications.objects.get(id=id)
    return render(request, "notifications/notification_detail.html",{"notification": notification})