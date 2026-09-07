from django.shortcuts import render, redirect
from django.utils import timezone
from rutcl import validar_rut
from .models import Visita
from .forms import VisitaForm

# CREATE - Registrar una visita
def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            rut_ingresado = form.cleaned_data['rut']

            # Estructura de decisión: validamos el RUT con el paquete externo
            if validar_rut(rut_ingresado):
                form.save()
                return redirect('listado_visitas')
            else:
                form.add_error('rut', 'El RUT ingresado no es válido.')
    else:
        form = VisitaForm()

    return render(request, 'visitas/registrar_visita.html', {'form': form})


# READ - Listado de visitas del día
def listado_visitas(request):
    hoy = timezone.now().date()
    visitas = Visita.objects.filter(hora_entrada__date=hoy)
    return render(request, 'visitas/listado_visitas.html', {'visitas': visitas})