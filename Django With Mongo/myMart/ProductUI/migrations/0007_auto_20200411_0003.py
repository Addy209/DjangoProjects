# Generated by Django 2.2.11 on 2020-04-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductUI', '0006_auto_20200411_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specifications',
            name='id',
        ),
        migrations.AlterField(
            model_name='specifications',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='specs', serialize=False, to='ProductUI.Products'),
        ),
    ]
