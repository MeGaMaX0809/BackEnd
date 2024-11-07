from django import forms
from .models import Luchador

class LuchadorForm(forms.ModelForm):
    class Meta:
        model = Luchador
        fields = ['nombre', 'categoria', 'peso', 'altura', 'nacionalidad', 'record', 'imagen']

    # Validación personalizada para el campo 'record'
    def clean_record(self):
        record = self.cleaned_data.get('record')
        partes = record.split('-')  # Cambié de '_' a '-' para que coincida con tu formato
        if len(partes) != 3 or not all(part.isdigit() for part in partes):
            raise forms.ValidationError("El récord debe estar en el formato 'Victorias-Derrotas-Empates'.")
        return record

    # Validación personalizada para el campo 'peso'
    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso <= 0:
            raise forms.ValidationError("El peso debe ser un número positivo.")
        return peso

    # Validación personalizada para el campo 'altura'
    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura <= 0:
            raise forms.ValidationError("La altura debe ser un número positivo.")
        return altura
