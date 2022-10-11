from django.urls import path
from .views import Scores

urlpatterns = [
    path('', Scores.as_view(), name='scores'),
]