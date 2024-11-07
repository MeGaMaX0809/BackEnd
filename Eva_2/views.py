# Eva_2/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Luchador
from .forms import LuchadorForm

def inicio(request):
    return render(request, 'luchadores/index.html')  # Renderiza la plantilla de inicio

def listar_luchador(request):
    luchadores = Luchador.objects.all()
    return render(request, 'luchadores/lista.html', {'luchadores': luchadores})

def crear_luchador(request):
    if request.method == 'POST':
        form = LuchadorForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES para imágenes
        if form.is_valid():
            form.save()
            print("Luchador guardado:", form.cleaned_data)
            return redirect('listar_luchadores')
    else:
        form = LuchadorForm()
    return render(request, 'luchadores/form.html', {'form': form})

def editar_luchador(request, luchador_id):
    luchador = get_object_or_404(Luchador, id=luchador_id)
    if request.method == 'POST':
        form = LuchadorForm(request.POST, request.FILES, instance=luchador)
        if form.is_valid():
            # Verificamos si el usuario marcó el checkbox para eliminar la imagen
            if 'eliminar_imagen' in request.POST:
                luchador.imagen.delete(False)  # Borra la imagen en la base de datos, pero no en el sistema de archivos
            form.save()  # Guarda los cambios del luchador
            return redirect('listar_luchadores')
    else:
        form = LuchadorForm(instance=luchador)
    return render(request, 'luchadores/form.html', {'form': form})

def eliminar_luchador(request, luchador_id):
    luchador = get_object_or_404(Luchador, id=luchador_id)
    luchador.delete()
    return redirect('listar_luchadores')
