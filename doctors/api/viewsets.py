from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import DoctorsSerializer
from doctors.models import Doctors

class DoctorsViewSet(viewsets.ModelViewSet):
    queryset= Doctors.objects.all()
    serializer_class = DoctorsSerializer