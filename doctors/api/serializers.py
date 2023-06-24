from rest_framework import serializers
from doctors.models import Doctors


class DoctorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctor_id','doctor_first_name','doctor_last_name','doctor_type_blood']