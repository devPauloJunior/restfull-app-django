from django.contrib import admin
from .models import Patients

class ListPatients(admin.ModelAdmin):
    list_display = ('patient_id','patient_last_name','patient_first_name','patient_type_blood')

admin.site.register(Patients, ListPatients)
