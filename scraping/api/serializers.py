from rest_framework import serializers
from scraping.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'price', 'km_number', 'brand')
