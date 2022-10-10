from django.contrib import admin
from .models import TypeNotification, Notification

# Register your models here.
admin.site.register(TypeNotification)
admin.site.register(Notification)