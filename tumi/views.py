from django.shortcuts import render
from .models import inspeccionInfo
from django.http import FileResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser
import random
import os
from twilio.rest import Client
from django.contrib.auth.decorators import login_required


codigo = ""
for i in range(6):
    codigo = codigo + str(random.randint(0,9))
verification_code = codigo
usuarioLocal = ''
contraLocal = ''

# Create your views here.
def index(request):
    return render(request,'login.html')

@login_required(login_url='/tumi')
def dashboard(request):
    return render(request,'dashboard.html',{
        'inspecciones':inspeccionInfo.objects.all().order_by('id'),
    })

@login_required(login_url='/tumi')
def descargarInforme(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    informe = open(inspeccion.informeUrl,'rb')
    return FileResponse(informe,as_attachment=True)

@login_required(login_url='/tumi')
def descargarLas(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    archivoLas = open(inspeccion.archivoLas,'rb')
    return FileResponse(archivoLas,as_attachment=True)

@login_required(login_url='/tumi')
def descargarDxf(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    archivoDxf = open(inspeccion.archivoDxf,'rb')
    return FileResponse(archivoDxf,as_attachment=True)

def consultarUsuario(request):
    global verification_code
    global usuarioLocal
    global contraLocal
    username = request.GET.get('username')
    contraUser = request.GET.get('contraUser')
    usuario_unico = authenticate(request,username=username,password=contraUser)
    print(usuario_unico)
    if usuario_unico is not None:
        codigoAleatorio = ""
        for i in range(6):
            codigoAleatorio = codigoAleatorio + str(random.randint(0,9))
        print(codigoAleatorio)
        account_sid = 'ACa320b3c57138262ff6c01583d663baf6'
        auth_token = '4b01bfb2ebebfcf58439c96d255da98d'
        cliente = Client(account_sid,auth_token)
        usuario_acceso = CustomUser.objects.get(username=username)
        message = cliente.messages.create(
            body= f"Welcome to TumiRobotics, your verification code is {codigoAleatorio}",
            from_="+19786263159",
            to="+51" + str(usuario_acceso.phone_number)
        )
        verification_code = codigoAleatorio
        usuarioLocal = username
        contraLocal = contraUser
        return JsonResponse({
            'resp':'200'
        })
    else:
        return JsonResponse({
            'resp':'404'
        })

def verificarCodigoUsuario(request):
    global verification_code
    global usuarioLocal
    global contraLocal
    codigoCelular = request.GET.get('codigoCelular')
    print(codigoCelular)
    if codigoCelular == verification_code:
        usuario_logueado = authenticate(request,username=usuarioLocal,password=contraLocal)
        login(request,usuario_logueado)
        return JsonResponse({
            'resp':'200',
        })
    else:
        return JsonResponse({
            'resp':'404',
        })
