# Generated by Django 2.2.11 on 2020-04-10 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductUI', '0005_auto_20200411_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='specifications',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specifications',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='ProductUI.Products', unique=True),
        ),
    ]