from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_visita, name='registrar_visita'),
    path('listado/', views.listado_visitas, name='listado_visitas'),
]