from django import forms
from django.forms.widgets import SelectDateWidget
from datetime import datetime

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    year = forms.TypedChoiceField(
        label='Year',
        coerce=int,
        choices=[(year, str(year)) for year in range(datetime.now().year, 1969, -1)]
    )

    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('user',)
