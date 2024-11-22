from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from Eva_2.models import Luchador
from .forms import EventoForm


# Vista para listar eventos
def listar_eventos(request):
    eventos = Evento.objects.all()  # Obtener todos los eventos
    return render(request, "eventos/lista.html", {"eventos": eventos})


# Vista para crear un evento
def crear_evento(request):
    if request.method == "POST":
        form = EventoForm(
            request.POST, request.FILES
        )  # Incluye request.FILES si hay campos de archivo
        if form.is_valid():
            evento = form.save()  # Guarda el evento principal
            if hasattr(form, "save_m2m"):  # Asegúrate de que save_m2m esté disponible
                form.save_m2m()  # Guarda las relaciones Many-to-Many
            return redirect("listar_eventos")  # Redirige a la lista de eventos
    else:
        form = EventoForm()
        form.fields["luchadores"].queryset = (
            Luchador.objects.all()
        )  # Poblamos el queryset de luchadores
    return render(request, "eventos/formulario.html", {"form": form})


# Vista para editar un evento
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()  # Solo guardamos el evento, no es necesario llamar a form.save_m2m()
            return redirect('listar_eventos')  # Redirigimos al listado de eventos
    else:
        form = EventoForm(instance=evento)
    
    form.fields['luchadores'].queryset = Luchador.objects.all()  # Asegúrate de que los luchadores estén disponibles en el formulario
    return render(request, 'eventos/formulario.html', {'form': form})


# Vista para eliminar un evento
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    return redirect("listar_eventos")


def evento_detalle(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, "eventos/detalle.html", {"evento": evento})
