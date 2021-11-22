# Generated by Django 3.2.8 on 2021-11-20 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_vendor_id'),
        ('client', '0013_alter_order_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.order'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='Product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
