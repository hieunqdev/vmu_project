from django.shortcuts import render, redirect
from django.views import View
from .models import TypeNotification, Notification
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.


class Home(View):
    def get(self, request):
        context = {
            'users': request.user
        }
        return render(request, 'home.html', context)

    def logout(self, request):
        logout(request)
        return redirect('index')


class Index(View):
    def get(self, request):
        notifications = TypeNotification.objects.raw(
            'SELECT news_typenotification.name AS type, news_notification.name AS news, news_notification.id FROM news_typenotification INNER JOIN news_notification ON news_typenotification.id = news_notification.type_id;')
        context = {
            'notifications': notifications
        }
        return render(request, 'index.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu sai')
            return redirect('/')


class News(View):
    def get(self, request):
        notifications = Notification.objects.values(
            'name', 'create_date', 'update_date', 'file_content')
        users = request.user
        context = {
            'notifications': notifications,
            'users': users
        }
        return render(request, 'news.html', context)