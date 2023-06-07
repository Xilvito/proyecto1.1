#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns =[
    path('index.html', views.index, name='index'),
    path('actualizar.html', views.actualizar, name='actualizar'),
    path('Asia.html', views.Asia, name='Asia'),
    path('carga.html', views.carga, name='carga'),
    path('Chile.html', views.Chile, name='Chile'),
    path('contacto.html', views.contacto, name='contacto'),
    path('crear.html', views.crear, name='crear'),
    path('destinos.html', views.destinos, name='destinos'),
    path('Europa.html', views.Europa, name='Europa'),
    path('indexEjecutivo.html', views.indexEjecutivo, name='indexEjecutivo'),
    path('inicioSesion.html', views.inicioSesion, name='inicioSesion'),
    path('reporte.html', views.reporte, name='reporte'),
    path('subir.html', views.subir, name='subir'),
]