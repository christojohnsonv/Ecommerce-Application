from django.db import models

# Create your models here.

class vendor(models.Model):
    vname=models.CharField(max_length=40,null=True)
    vemail=models.EmailField(max_length=40,null=True)
    vpassword=models.CharField(max_length=40,null=True)
    vbranch=models.CharField(max_length=40,null=True)
    vurl=models.CharField(max_length=40,null=True)
    vaddress=models.CharField(max_length=40,null=True)
    vphone=models.IntegerField(null=True)
    vgst=models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.vname