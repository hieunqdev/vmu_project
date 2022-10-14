from django.contrib import admin
from .models import TypeNotification, Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'create_date', 'update_date']
    list_filter = ['name', 'type', 'create_date', 'update_date']

admin.site.register(TypeNotification)
admin.site.register(Notification, NotificationAdmin)