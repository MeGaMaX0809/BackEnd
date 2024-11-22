from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('<int:evento_id>/', views.evento_detalle, name='evento_detalle'),
    path('nuevo/', views.crear_evento, name='crear_evento'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    
]
