from rest_framework import routers
from django.urls import path, include

from axis.viewsets import AxleViewSet


router = routers.DefaultRouter()
router.register(r'eixos', AxleViewSet, basename='axles')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
