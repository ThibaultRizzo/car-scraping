from rest_framework import viewsets

from scraping.models import Car
from scraping.api.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
