# example/urls.py
from django.urls import path

from mywebsite.views import home


urlpatterns = [
    path('', home),
]