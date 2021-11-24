from os import truncate
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import CASCADE
from product.models import product
from vendor.models import vendor


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    created_at=models.DateTimeField(null=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    postcode=models.IntegerField(null=True,default=None)
    gender=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    phone=models.IntegerField(null=True)
    image=models.ImageField(upload_to='images/',default='media/Image.jpg')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserManager()

    def get_username(self):
        return self.email


class order(models.Model):
    order_number=models.CharField(max_length=40,null=True)
    order_date=models.DateTimeField(null=True)
    order_total=models.IntegerField(null=True)
    customer_id=models.ForeignKey(User,on_delete=CASCADE,null=True)
    delivery_date=models.DateField(null=True)
    is_delivered=models.DateField(null=True)
    vendor_id=models.ForeignKey(vendor,on_delete=CASCADE,null=True)

    def __str__(self):
        return self.order_number









class order_details(models.Model):
    Product_id=models.ForeignKey(product,on_delete=CASCADE,null=True)
    Product_quantity=models.IntegerField(null=True)
    Product_Price=models.IntegerField(null=True)
    order_id=models.ForeignKey(order,on_delete=CASCADE,null=True)
    Subtotal=models.IntegerField(null=True)
    Payment_methos=models.CharField(max_length=40,null=True)
    Paymrnt_status=models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.Product_id









class cart(models.Model):
    product_id=models.CharField(max_length=40,null=True)
    product_no=models.IntegerField(null=True)
    email_id=models.EmailField(null=True)
    