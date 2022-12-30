from django.urls import path
from . import views

app_name='tumi'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('descargarInforme/<str:ind>',views.descargarInforme,name='descargarInforme'),
    path('descargarLas/<str:ind>',views.descargarLas,name='descargarLas'),
    path('descargarDxf/<str:ind>',views.descargarDxf,name='descargarDxf'),
    path('consultarUsuario',views.consultarUsuario,name='consultarUsuario'),
    path('verificarCodigoUsuario',views.verificarCodigoUsuario,name='verificarCodigoUsuario'),
    path('log_out',views.log_out,name='log_out')
]