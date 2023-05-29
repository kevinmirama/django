from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('formulario/', views.mostrar_formulario, name='mostrar_formulario'),
    path('buscar_actualizar_contacto/', views.buscar_actualizar_contacto, name='buscar_actualizar_contacto'),
    # ...
]