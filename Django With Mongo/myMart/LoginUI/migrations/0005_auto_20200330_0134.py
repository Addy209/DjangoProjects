# Generated by Django 2.2.11 on 2020-03-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUI', '0004_auto_20200330_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_name',
            field=models.CharField(max_length=20),
        ),
    ]
