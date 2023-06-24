from django.db import models

class Doctors(models.Model):
    doctor_id = models.BigAutoField(primary_key=True)
    doctor_first_name= models.CharField(max_length=50)
    doctor_last_name= models.CharField(max_length=50)
    doctor_type_blood= models.CharField(max_length=50)

    def __str__(self):
        return str(self.doctor_id)