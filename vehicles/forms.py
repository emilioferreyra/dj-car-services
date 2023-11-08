from django import forms
from .utils import select_vehicle_year  # Importa la función desde tu módulo de utilidades


class VehicleForm(forms.Form):
    # Utiliza la función select_vehicle_year para obtener la lista de años disponibles
    year_choices = [(year, year) for year in range(1970, select_vehicle_year() + 1)]

    # Define el campo IntegerField con las opciones de años
    vehicle_year = forms.IntegerField(
        label="Select Vehicle Year",
        widget=forms.Select(choices=year_choices)
    )
