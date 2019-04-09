from django import forms

from .models import Lot

class BookingForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    lot = forms.ModelChoiceField(queryset=Lot.objects.all())