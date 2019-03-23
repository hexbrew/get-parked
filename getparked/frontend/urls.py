from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import index

urlpatterns = [
    re_path(r'^(?:.*)/?$', index)
]
