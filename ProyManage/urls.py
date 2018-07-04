from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/', views.about),
    re_path(r'^$',views.home, name="home"),
    re_path(r'^accounts/',include('accounts.urls')),
    re_path(r'^proyects/',include('proyects.urls'))
]
