from unicodedata import name
from django import views
from django.urls import URLPattern, path, re_path

from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("<str:name>", views.greet, name="greet")
]