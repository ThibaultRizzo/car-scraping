# Generated by Django 2.1.5 on 2019-03-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20190226_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gear_box',
            field=models.CharField(max_length=50, null=True),
        ),
    ]