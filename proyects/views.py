from django.shortcuts import render, redirect
from .models import Task,TaskItem,TaskNote,TodoList,Project
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def lista_proy(request):
    proyects = Project.objects.all()

    return render(request,'proyects/list_proy.html',{'proyects': proyects})

def detalles_art(request):

    proyects = Project.objects.all()

    return render(request,'proyects/det_proy.html',{'proyects': proyects})

@login_required(login_url="/accounts/login/")
def create_proy (request):
    if request.method =='POST':
        form = forms.create_proyect(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('proyects:lista')
    else:
        form = forms.create_proyect()
    return render(request, 'proyects/create_proy.html', {'form':form})