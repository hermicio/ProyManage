from django.contrib import admin
from .models import Task,TaskItem,TaskNote,TodoList,Project
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskItem)
admin.site.register(TaskNote)
admin.site.register(TodoList)
admin.site.register(Project)
