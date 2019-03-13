from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
import math
from enum import Enum

from scraping.models import Car


class CarStatisticTitle(Enum):
    NB_REF_CAR = "Number of referenced cars"
    NB_RTL = "Number of retailers scraped"
    AVG_CAR_PRC = "Average Car Price"


class CarStatisticManager(models.Manager):
    def getLatestStats(self):
        stat_list = CarStatistic.objects.all().order_by(
            'title', '-created').distinct('title')
        return stat_list

    def getLastTrend(self, title, date, limit):
        older_stat_list = list(CarStatistic.objects.filter(
            title=title, created__lt=date).order_by('-created')[:limit])  # May need to add filter() to allow multiple records
        # If no previous record is found, None value is output
        return older_stat_list if len(older_stat_list) else None

    def computeTrend(self, title, date, number):
        # Compute the trend of current instance compared to the previous one
        last_trend = CarStatistic.objects.getLastTrend(title, date, 1)
        if last_trend is None:
            return 'FLAT'
        elif math.isclose(last_trend[0].number, number):
            return 'FLAT'
        elif last_trend[0].number < number:
            return 'ASCENDING'
        else:
            return 'DESCENDING'

    def create_or_update_stat(self, title, number, unit, description):
        try:
            stat = CarStatistic.objects.get(
                title=title, created=datetime.date.today())
            stat.number = number
            stat.unit = unit
            stat.description = description
            stat.save()
        except CarStatistic.DoesNotExist:
            stat = CarStatistic.objects.create(
                title=title, number=number, unit=unit, description=description)

    def processCarStatistics(self, title_tuple):
        for title in title_tuple:
            if(CarStatisticTitle.NB_REF_CAR == title):
                CarStatistic.objects.create_or_update_stat(
                    CarStatisticTitle.NB_REF_CAR, Car.objects.get_car_count(), 'voitures', '')
            elif(CarStatisticTitle.NB_RTL == title):
                CarStatistic.objects.create_or_update_stat(
                    CarStatisticTitle.NB_RTL, Car.objects.get_retailer_count(), 'retailers', '')
            elif(CarStatisticTitle.AVG_CAR_PRC == title):
                CarStatistic.objects.create_or_update_stat(
                    CarStatisticTitle.AVG_CAR_PRC, Car.objects.get_avg_car_price(), '$', '')


class CarStatistic(models.Model):
    Trend = (
        ('ASC', 'ASCENDING'),
        ('DESC', 'DESCENDING'),
        ('FLAT', 'FLAT')
    )
    title = models.CharField(
        max_length=100)
    title = models.CharField(max_length=50, choices=[(
        tag, tag.value) for tag in CarStatisticTitle])
    created = models.DateField(auto_now=True)
    number = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100)
    trend = models.CharField(max_length=10, choices=Trend, default='FLAT')
    objects = CarStatisticManager()

    class Meta:
        unique_together = (('title', 'created'),)


@receiver(pre_save, sender=CarStatistic)
def setup_Trend(sender, instance, **kwargs):
    instance.trend = CarStatistic.objects.computeTrend(
        instance.title, datetime.date.today(), instance.number)
