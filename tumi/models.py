from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class inspeccionInfo(models.Model):
    fechaInspeccion = models.DateField(default=timezone.now)
    informeUrl = models.CharField(max_length=512,default='')
    videoUrl = models.CharField(max_length=512,default='')
    archivoLas = models.CharField(max_length=512,default='')
    archivoDxf = models.CharField(max_length=512,default='')
    nombreUnidadMinera = models.CharField(max_length=128,default='')
    nombreOperacion = models.CharField(max_length=128,default='')
    detalleInspeccion = models.CharField(max_length=128,default='')
    estadoInspeccion = models.CharField(max_length=128,default='')