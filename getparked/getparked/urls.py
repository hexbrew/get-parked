from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings

from parking import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    
    path('lots/', views.LotListView.as_view(), name='lot-list'),
    path('lots/<int:pk>/', views.LotDetailView.as_view(), name='lot-detail'),
    path('lots/<int:pk>/book/', views.book_lot, name='lot-booking'),


    path(settings.FRONTEND_URL, include('frontend.urls')),

    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
