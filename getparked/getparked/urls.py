from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings

from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(settings.FRONTEND_URL, include('frontend.urls')),
    path('parks/', views.car_park_availability)
]
