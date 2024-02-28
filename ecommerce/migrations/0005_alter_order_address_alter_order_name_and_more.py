# Generated by Django 5.0.2 on 2024-02-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_order_total_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=225),
        ),
    ]
