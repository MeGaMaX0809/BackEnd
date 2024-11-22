# BackEnd_2/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # 'include' es necesario para incluir otras URLs
from Eva_2.views import listar_luchador, crear_luchador, eliminar_luchador, editar_luchador, inicio  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
    path('luchadores/', listar_luchador, name='listar_luchadores'),
    path('luchadores/nuevo/', crear_luchador, name='crear_luchador'),
    path('editar/<int:luchador_id>/', editar_luchador, name='editar_luchador'),
    path('luchadores/eliminar/<int:luchador_id>/', eliminar_luchador, name='eliminar_luchador'),
    
    path('', include('eventos.urls')),  # Incluye las URLs de la app eventos
    # Incluir las URLs de la app 'eventos'
    path('eventos/', include('eventos.urls')),  # Esto incluye todas las URLs definidas en eventos/urls.py
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    