# Generated by Django 2.1.5 on 2019-02-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_auto_20190226_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='gear_box',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='motor_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='petrol_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='reg_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='reg_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='vendor_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='vendor_ref',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
