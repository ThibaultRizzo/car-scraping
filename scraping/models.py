from django.db import models

# Create your models here.


class TestCar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class Car(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    km_number = models.IntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now=False, null=True)
    gear_box = models.CharField(max_length=10, null=True)
    motor_type = models.CharField(max_length=10, null=True)
    petrol_type = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, null=True)
    doors_number = models.IntegerField(null=True)
    vendor_link = models.CharField(max_length=100, null=True)
    vendor_ref = models.CharField(max_length=50, null=True)
    owner_number = models.IntegerField(null=True)
    reg_number = models.CharField(max_length=10, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
