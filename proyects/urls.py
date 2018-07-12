from django.urls import path, re_path
from . import views

app_name = 'proyects'

urlpatterns = [
    re_path(r'^lista/$', views.lista_proy, name='lista'),
    re_path(r'^crear/$', views.create_proy, name='crear'),
    #re_path(r'^proy(?P<shortname>+)/$', views.detalles_art,name ='detalle'),
    re_path(r'^detalle/(?P<shortname>[\w-]+)$', views.detalles_proy, name='detalle'),
    #re_path(r'^(?P<proy>[\w-]+)/$', views.create_task,name ='crear_task')
    #re_path(r'^(/taskhistory/ + ?P<proy>[\w-])/$', views.create_task , 'crear_task'),

]
