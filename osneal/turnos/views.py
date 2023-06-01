from django.shortcuts import render
from django.http import JsonResponse
from .models import Turno
from .forms import TurnoForm
from mascotas.models import Mascota
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('turnos.add_turno',raise_exception=True)
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

        if not mascota:
            return JsonResponse({"mensaje" : {"Error":"El número de microchip no existe"}},status=400)

        request.POST._mutable = True
        request.POST['mascota'] = mascota.pk
        form = TurnoForm(request.POST, initial={'mascota': mascota})

        if not form.is_valid():
            return JsonResponse({"mensaje" : form.errors},status=400)

        form.save()

        return JsonResponse({},status=201)
    else:
        return JsonResponse({"mensaje":"Este método no está permitido"},status=403)


@login_required
@permission_required('turnos.view_turno',raise_exception=True)
def obtener_turnos(request):
    if request.method == 'GET':
        turnos = Turno.objects.all()
        print(request.user.tipo_usuario)
        if request.user.tipo_usuario == 'propietario':
            turnos = turnos.filter(mascota__duenio=request.user)
        turnos_json = []
        for turno in turnos:
            turnos_json.append({
                'id': turno.pk,
                'mascota': turno.mascota.nombre,
                'title': turno.descripcion_corta,
                'descripcion': turno.descripcion,
                'tipo_turno': turno.tipo_turno,
                'start': turno.inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': turno.fin.strftime("%Y-%m-%dT%H:%M:%S")
            })
        return JsonResponse(turnos_json,status=200,safe=False)
    else:
        return JsonResponse({"mensaje":"Este método no está permitido"},status=403)


@login_required
@permission_required('turnos.delete_turno',raise_exception=True)
def borrar_turno(request):
    if request.method == 'POST':
        id_turno = request.POST.get('id_turno')
        print(id_turno)
        turno = Turno.objects.filter(pk=id_turno).first()
        if turno:
            turno.delete()
            return JsonResponse({},status=200)
        else:
            return JsonResponse({"mensaje" : {"Error":"El turno no existe"}},status=400)
    else:
        return JsonResponse({"mensaje":"Este método no está permitido"},status=403)
