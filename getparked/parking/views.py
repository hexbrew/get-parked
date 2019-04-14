from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.utils import timezone
from django.views.generic import View, ListView, DetailView, FormView

from .models import DAYS, Lot


class LotListView(ListView):
    model = Lot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LotDetailView(DetailView):
    model = Lot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DAYS'] = DAYS
        return context


def book_lot(request, pk):
    print(pk)
    lot = Lot.objects.get(pk=pk)
    return TemplateResponse(request, 'parking/lot_booking.html', {'lot': lot})
