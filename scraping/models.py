from django.db import models
from django.db.transaction import atomic


class CarManager(models.Manager):
    def get_all_model(self, vendor):
        return Car.objects.filter(vendor=vendor).order_by('model').values('model', 'brand').distinct()

    def get_car_count(self):
        return Car.objects.count()

    def get_number_of_model(self, model):
        return Car.objects.filter(model=model).count()

    @atomic
    def save_as_batch(self, queryset):
        for item in queryset:
            item.save()

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
    km_number = models.IntegerField(default=0)
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
    created = models.DateTimeField(auto_now=True)
    objects = CarManager()

    class Meta:
        ordering = ('created',)
