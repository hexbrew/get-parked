from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import DAYS, Lot


class LotListView(ListView):
    model = Lot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class LotDetailView(DetailView):
    model = Lot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DAYS'] = DAYS
        return context