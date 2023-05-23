from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import PatientsSerializer
from bloodbank.models import Patients

class PatientsViewSet(viewsets.ModelViewSet):
    queryset= Patients.objects.all()
    serializer_class = PatientsSerializer