from django.db import models
from django.contrib.auth.models import User
from django import forms

unit_choices = (
    ('Hours', 'Hours'),
    ('Days', 'Days'),
    ('Months', 'Months'),
    )

class Project(models.Model):

    shortname = models.CharField(max_length = 20, unique = True)
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null = True)
    is_active = models.BooleanField(default = True)
    created_on = models.DateTimeField(auto_now_add = 1)

    def __str__(self):
        return self.name


class Task(models.Model):
    #tareas
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, default=None,on_delete=models.CASCADE)
    parent_task_num = models.IntegerField(null=True, blank=True) # si tiene id de tarea es una subtarea
    user_responsible = models.ForeignKey(User, null=True, blank=True, default=None,on_delete=models.CASCADE)#responsable de la tarea
    expected_start_date = models.DateField() #Estimado de inicio
    expected_end_date = models.DateField(null=True, blank=True) #Estimado de fin
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False) #tarea completada
    created_on = models.DateTimeField(auto_now_add=1) #fecha creacion
    is_deleted = models.BooleanField(default=False) #marcada como eliminada
    created_by = models.ForeignKey(User, related_name='created_tasks', default=None,on_delete=models.CASCADE)
    last_updated_by = models.ForeignKey(User, related_name='updated_tasks', default=None,on_delete=models.CASCADE)
    # Versioning
    effective_start_date = models.DateTimeField(auto_now_add=True)
    effective_end_date = models.DateTimeField(null=True, auto_now=True)
    version_number = models.IntegerField()
    is_current = models.BooleanField(default=True)


class TaskItem(models.Model):
    #sub tareas
    number = models.IntegerField()
    project = models.ForeignKey(Project, default=None,on_delete=models.CASCADE)
    task_num = models.IntegerField()
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, default=None,on_delete=models.CASCADE)
    expected_time = models.DecimalField(decimal_places=2, max_digits=10)
    actual_time = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    unit = models.CharField(max_length=20, choices=unit_choices)
    is_complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=1)
    created_by = models.ForeignKey(User, related_name='created_taskitems', default=None,on_delete=models.CASCADE)
    last_updated_by = models.ForeignKey(User, related_name='updated_taskitems', default=None,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    # Versioning
    effective_start_date = models.DateTimeField(auto_now_add=1)
    effective_end_date = models.DateTimeField(null=True)
    version_number = models.IntegerField()
    is_current = models.BooleanField(default=True)


class TodoList(models.Model):
    # lista de tareas de un usuario
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, default=None,on_delete=models.CASCADE)
    is_complete_attr = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add = 1)

class TaskNote(models.Model):
    #notas de tareas
    task_num = models.IntegerField()
    text = models.TextField()
    user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = 1)