from django.test import TestCase

import datetime
# from carstatistic.models import CarStatistic, CarStatisticTitle


def testSmt(l):
    l.append(1)


l = []
for i in [1, 2, 3, 4, 5]:
    testSmt(l)
print(l)
