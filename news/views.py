from django.shortcuts import render
from django.views import View
from .models import TypeNotification

# Create your views here.
class Index(View):
    def get(self, request):
        types_notifications = TypeNotification.objects.all()
        context = {
            'types_notifications': types_notifications
        }
        return render(request, 'index.html', context)