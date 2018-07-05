from django.forms import ModelForm, Textarea, TextInput, URLInput
from . import models



class create_proyect(ModelForm):
    class Meta:
        model = models.Project
        fields=['shortname','name','owner', 'start_date','end_date','is_active']

class create_task(ModelForm):
    class meta:
        model = models.Task
        fields=['name','project','parent_task_num','user_responsible','expected_start_date','expected_end_date','actual_start_date','actual_end_date','is_complete','created_on','is_deleted','created_by','last_updated_by']