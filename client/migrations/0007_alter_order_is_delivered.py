# Generated by Django 3.2.8 on 2021-11-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_delivered',
            field=models.DateField(null=True),
        ),
    ]
