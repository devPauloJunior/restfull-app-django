from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import PatientsViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientsViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]