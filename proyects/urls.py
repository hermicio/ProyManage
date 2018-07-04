from django.urls import path, re_path
from . import views

app_name = 'proyects'

urlpatterns = [
    re_path(r'^lista/$', views.lista_proy, name='lista'),
    re_path(r'^crear/$', views.create_proy, name='crear'),
    re_path(r'^detalle/$', views.detalles_art,name ='detalle'),

]
