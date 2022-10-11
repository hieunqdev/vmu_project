from unicodedata import name
from django.urls import path
from .views import View_training_programme

urlpatterns = [
    path('', View_training_programme.as_view(), name='view_training_programme'),
]