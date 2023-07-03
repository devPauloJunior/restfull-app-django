from django.db import models
from doctors.models import Doctors

class Patients(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_type_blood = models.CharField(max_length=50)
    patient_doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.patient_id)