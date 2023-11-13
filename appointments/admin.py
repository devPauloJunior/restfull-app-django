from django.contrib import admin
from .models import Appointments

class ListAppointments(admin.ModelAdmin):
    list_display = ('appointments_id', 'appointments_doctor', 'appointments_patient', 'appointments_title', 'appointments_desc', 'appointments_date')

admin.site.register(Appointments, ListAppointments)
