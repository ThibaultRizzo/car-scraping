from django.db import models
from django.db.transaction import atomic


class CarManager(models.Manager):
    def get_all_vendors(self):
        return map(lambda el: el["vendor"], list(Car.objects.values('vendor').order_by('vendor').distinct('vendor')))

    def get_all_brands(self):
        return map(lambda el: el["brand"], list(Car.objects.values('brand').order_by('brand').distinct('brand')))

    def get_all_models(self, vendor, *fields):
        return list(Car.objects.order_by('brand').values('model', 'brand', *fields).distinct('brand'))

    def get_all_models_per_brand(self, brand, fields):
        return Car.objects.filter(brand=brand).order_by('model').values('model', *fields).distinct()

    def get_all_models_per_vendor(self, vendor):
        return Car.objects.filter(vendor=vendor).order_by('model').values('model', 'brand').distinct()

    def get_retailer_count(self):
        return Car.objects.values('vendor').distinct().count()

    def get_avg_car_price(self):
        return Car.objects.aggregate(models.Avg('price'))['price__avg']

    def get_avg_car_price(self):
        return Car.objects.aggregate(models.Avg('price'))['price__avg']

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
        max_length=100, unique=True, primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    km_number = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now=False, null=True)
    gear_box = models.CharField(max_length=100, null=True)
    gear_number = models.CharField(max_length=100, null=True)
    motor_type = models.CharField(max_length=100, null=True)
    petrol_type = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    doors_number = models.CharField(max_length=20, null=True)
    vendor_link = models.CharField(max_length=500, null=True)
    owner_number = models.IntegerField(null=True)
    reg_number = models.CharField(max_length=100, null=True, unique=True)
    created = models.DateTimeField(auto_now=True)
    objects = CarManager()

    class Meta:
        ordering = ('created',)

    def get_fields():
        return list(map(lambda field: field.name, Car._meta.local_fields))
