from django.contrib import admin
from .models import Doctors

class ListDoctors(admin.ModelAdmin):
    list_display = ('doctor_id','doctor_last_name','doctor_first_name','doctor_type_blood')

admin.site.register(Doctors, ListDoctors)