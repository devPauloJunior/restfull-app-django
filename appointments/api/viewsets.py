from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import AppointmentsSerializer
from appointments.models import Appointments

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset= Appointments.objects.all()
    serializer_class = AppointmentsSerializer