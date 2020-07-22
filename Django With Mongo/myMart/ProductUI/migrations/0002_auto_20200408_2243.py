# Generated by Django 2.2.11 on 2020-04-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductUI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pic',
            field=models.ImageField(blank=True, upload_to='product_pic'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Grocery', 'Grocery'), ('Home Decor', 'Home Decor'), ('Kids', 'Kids'), ('Beauty', 'Beauty'), ('Sports', 'Sports'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
