from django.db import models

# Create your models here.


class TestCar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class CarManager(models.Manager):
    def delete_everything(self):
        Car.objects.all().delete()

    def drop_table(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            table_name = self.model._meta.db_table
            sql = "DROP TABLE %s;" % (table_name, )
            cursor.execute(sql)


class Car(models.Model):
    # TODO: Add currency and distance measure
    vendor_ref = models.CharField(
        max_length=50, unique=True, primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    km_number = models.IntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now=False, null=True)
    gear_box = models.CharField(max_length=50, null=True)
    gear_number = models.CharField(max_length=50, null=True)
    motor_type = models.CharField(max_length=10, null=True)
    petrol_type = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, null=True)
    doors_number = models.CharField(max_length=20, null=True)
    vendor_link = models.CharField(max_length=100, null=True)
    owner_number = models.IntegerField(null=True)
    reg_number = models.CharField(max_length=10, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = CarManager()

    class Meta:
        ordering = ('created',)
