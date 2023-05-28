from django.shortcuts import render
from django.http import JsonResponse
from .models import Turno
from .forms import TurnoForm
from mascotas.models import Mascota


def crear_turno(request):
    if request.method == 'POST':

        mascota = request.POST.get('mascota')

        if not mascota.find(" - ") == -1:
            microchip = mascota.split(" - ")[0]
        elif mascota.isnumeric():
            microchip = mascota
        else:
            return JsonResponse({"mensaje" : {"Error":"El número de microchip no existe"}},status=400)

        mascota = Mascota.objects.filter(micro_chip=microchip).first()

        request.POST._mutable = True
        request.POST['mascota'] = mascota.pk #este era el problema ver como solucionar
        form = TurnoForm(request.POST, initial={'mascota': mascota})

        if not form.is_valid():
            return JsonResponse({"mensaje" : form.errors},status=400)

        form.save()

        return JsonResponse({},status=201)
    else:
        return JsonResponse({},status=400)
