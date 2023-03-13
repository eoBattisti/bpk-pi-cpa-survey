from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
