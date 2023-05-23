from rest_framework import serializers
from bloodbank.models import Patients


class PatientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patients
        fields = ['patient_id','patient_first_name','patient_last_name','patient_type_blood']