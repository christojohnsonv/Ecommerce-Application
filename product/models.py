from django.db import models
from django.db.models.deletion import CASCADE
import pandas as pd
import os
from pathlib import Path
from vendor.models import *
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your models here.

class category(models.Model):
    category_name=models.CharField(max_length=40,null=True)
    category_image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.category_name


class product(models.Model):
    product_name=models.CharField(max_length=40,null=True)
    product_image1=models.ImageField(upload_to='images/',null=True)
    product_image2=models.ImageField(upload_to='images/',null=True)
    product_image3=models.ImageField(upload_to='images/',null=True)
    product_description=models.CharField(max_length=40,null=True)
    price=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)
    pcategory=models.ForeignKey(category,on_delete=CASCADE,null=True)
    stock_status=models.CharField(max_length=40,null=True)
    vendor_id=models.ForeignKey(vendor,on_delete=CASCADE,null=True)

    def __str__(self):
        return self.product_name
