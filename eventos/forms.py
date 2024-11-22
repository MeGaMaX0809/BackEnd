from django import forms
from .models import Evento
from Eva_2.models import Luchador

class EventoForm(forms.ModelForm):
    
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # Muestra un selector de fecha
            'class': 'form-control',  # Agrega estilos CSS (si los usas)
            'placeholder': 'YYYY-MM-DD',  # Mensaje de ayuda
        }),
        input_formats=['%Y-%m-%d'],  # Formato aceptado
    )
    
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'lugar', 'imagen', 'luchadores']

    luchadores = forms.ModelMultipleChoiceField(
        queryset=Luchador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # No es obligatorio asignar luchadores
    )
