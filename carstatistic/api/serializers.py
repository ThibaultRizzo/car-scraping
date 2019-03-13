from rest_framework import serializers
from carstatistic.models import CarStatistic


class CarStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatistic
        exclude = ['id']
