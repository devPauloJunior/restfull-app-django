from django.db import models
from doctors.models import Doctors
from bloodbank.models import Patients

class Appointments(models.Model):
    appointments_id = models.BigAutoField(primary_key=True)
    appointments_doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointments_patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    appointments_title = models.CharField(max_length=60)
    appointments_desc = models.CharField(max_length=150)

    def __str__(self):
        return str(self.appointments_id)