from rest_framework import serializers
from appointments.models import Appointments


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['appointments_id', 'appointments_doctor', 'appointments_patient', 'appointments_title', 'appointments_desc', 'appointments_date']