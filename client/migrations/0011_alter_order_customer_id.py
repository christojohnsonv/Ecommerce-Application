# Generated by Django 3.2.8 on 2021-11-19 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]