from django import forms
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Lot, Bay, Booking, BookingDay


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking

class LotAddForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ['location', 'monthly_rate']
        help_texts = {
            'location': _('The address of this lot.'),
            'monthly_rate': _("The default monthly rate to apply for customers who sign up online.")
        }

    unreserved_bays = forms.IntegerField(label="Number of unreserved bays", help_text=_(
        "You will be able to customise these further after lot creation."))
    reserved_bays = forms.IntegerField(label="Number of reserved bays", help_text=_(
        "You will be able to customise these further after lot creation."))

    def save(self, commit=True):
        instance = super(LotAddForm, self).save(commit=False)
        instance.save()

        for i in range(self.cleaned_data['unreserved_bays']):
            Bay.objects.create(lot=instance)

        for i in range(1, self.cleaned_data['reserved_bays'] + 1):
            Bay.objects.create(lot=instance, code=i)

        return instance
