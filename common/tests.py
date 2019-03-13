from django.test import TestCase

import datetime
from carstatistic import models
# from carstatistic.models import CarStatistic, CarStatisticTitle

print(CarStatistic.objects.getLastTrend(
    CarStatisticTitle.NB_REF_CAR, datetime.date.today(), 1))
