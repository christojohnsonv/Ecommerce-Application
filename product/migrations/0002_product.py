# Generated by Django 3.2.8 on 2021-11-16 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40, null=True)),
                ('product_image1', models.ImageField(null=True, upload_to='images/')),
                ('product_image2', models.ImageField(null=True, upload_to='images/')),
                ('product_image3', models.ImageField(null=True, upload_to='images/')),
                ('product_description', models.CharField(max_length=40, null=True)),
                ('price', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('stock_status', models.CharField(max_length=40, null=True)),
                ('vendor_id', models.FloatField(max_length=40, null=True)),
                ('pcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
