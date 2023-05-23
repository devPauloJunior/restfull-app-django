from django.db import models

class Patients(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    patient_first_name= models.CharField(max_length=50)
    patient_last_name= models.CharField(max_length=50)
    patient_type_blood= models.CharField(max_length=50)

    def __str__(self):
        return self.patient_first_name