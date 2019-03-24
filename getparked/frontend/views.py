from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        'path': settings.FRONTEND_URL,
    }
    print(context)
    return render(request, 'index.html', context)
