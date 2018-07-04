from django.forms import ModelForm, Textarea, TextInput, URLInput
from . import models



class create_proyect(ModelForm):
    class Meta:
        model = models.Project
        fields=['shortname','name','owner', 'start_date','end_date','is_active']