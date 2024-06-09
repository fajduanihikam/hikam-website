# example/urls.py
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mywebsite.views import home

urlpatterns = [
    path('', home),
]
urlpatterns += staticfiles_urlpatterns()