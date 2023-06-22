from rest_framework import serializers
from doctors.models import Doctors


class DoctorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctors_id','doctors_first_name','doctors_last_name','doctors_type_blood']