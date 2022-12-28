from django.shortcuts import render
from .models import inspeccionInfo
from django.http import FileResponse

# Create your views here.
def index(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html',{
        'inspecciones':inspeccionInfo.objects.all().order_by('id'),
    })

def descargarInforme(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    informe = open(inspeccion.informeUrl,'rb')
    return FileResponse(informe,as_attachment=True)

def descargarLas(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    archivoLas = open(inspeccion.archivoLas,'rb')
    return FileResponse(archivoLas,as_attachment=True)

def descargarDxf(request,ind):
    inspeccion = inspeccionInfo.objects.get(id=ind)
    archivoDxf = open(inspeccion.archivoDxf,'rb')
    return FileResponse(archivoDxf,as_attachment=True)