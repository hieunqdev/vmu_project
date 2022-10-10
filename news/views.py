from django.shortcuts import render
from django.views import View
from psycopg2 import connect
from .models import TypeNotification, Notification
from django.db import connection

# Create your views here.
class Index(View):
    def get(self, request):
       notifications = TypeNotification.objects.raw('SELECT news_typenotification.name AS type, news_notification.name AS news, news_notification.id FROM news_typenotification INNER JOIN news_notification ON news_typenotification.id = news_notification.type_id;')
       context = {
            'notifications': notifications
       }
       return render(request, 'index.html', context)

class News(View):
    def get(self, request):
        notifications = Notification.objects.values('name', 'create_date', 'update_date', 'file_content')
        context = {
            'notifications': notifications
        }
        return render(request, 'news.html', context)
