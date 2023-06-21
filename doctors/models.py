from django.db import models

class Doctors(models.Model):
    doctors_id = models.BigAutoField(primary_key=True)
    doctors_first_name= models.CharField(max_length=50)
    doctors_last_name= models.CharField(max_length=50)
    doctors_type_blood= models.CharField(max_length=50)

    def __str__(self):
        return self.doctors_first_name