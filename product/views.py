from os import path
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from vendor.models import vendor
from .models import category

from django.core.files.storage import FileSystemStorage
from django.db.models.fields import files
from django.shortcuts import redirect, render
import pandas as pd

from product.models import category, product
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def addcat(request):
    if request.method=="POST":
        na=request.POST.get("name")
        im=request.FILES['image']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        category.objects.create(category_name=na,category_image=fp)
    return render(request,"addcat.html")


def discat(request):
    obj=category.objects.all()
    return render(request,"discat.html",{'datas':obj})





def addcat(request):
    if request.method=="POST":
        na=request.POST.get("name")
        im=request.FILES['image']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        category.objects.create(category_name=na,category_image=fp)
    return render(request,"addcat.html")


def addpro(request):
    obj=category.objects.all()
    ven=vendor.objects.all()
    if request.method=="POST":
        na=request.POST.get("product_name")
        im1=request.FILES['product_image1']
        im2=request.FILES['product_image2']
        im3=request.FILES['product_image3']
        f=FileSystemStorage()
        fp1=f.save(im1.name,im1)
        fp2=f.save(im2.name,im2)
        fp3=f.save(im3.name,im3)
        pd=request.POST.get("product_description")
        pr=request.POST.get("price")
        st=request.POST.get("stock")
        ct=request.POST.get("category")
        ca=category.objects.get(id=ct)
        ve=request.POST.get("vendor")
        vd=vendor.objects.get(id=ve)
        product.objects.create(product_name=na,product_image1=fp1,product_image2=fp2,product_image3=fp3,product_description=pd,price=pr,stock=st,pcategory=ca,vendor_id=vd)
    return render(request,"addpro.html",{'cat':obj,"vend":ven})

def discat(request):
    obj=category.objects.all()
    return render(request,"discat.html",{'datas':obj})

def dispro(request):
    obj=product.objects.all()
    df=pd.DataFrame(obj.values())
    path=os.path.join(BASE_DIR,'media/products.csv')
    df.to_csv(path)
    return render(request,"dispro.html",{"datas":obj})

def dispro(request):
    obj=product.objects.all()
    df=pd.DataFrame(obj.values())
    path=os.path.join(BASE_DIR,'media/products.csv')
    df.to_csv(path)
    return render(request,"dispro.html",{"datas":obj})


def filterpro(request):
    if request.method=="POST":
        by=request.POST.get("filter")
        key=request.POST.get("key")
        if by=="null":
            return redirect("dispro")
        else:
            if by=="name":
                result=product.objects.filter(product_name_contains=key)
            if by=="cat":
                result=product.objects.filter(pcategory__category=key)
            if by=="less":
                result=pd.DataFrame(product.objects.filter(price__lte=int(key)))
            if by=="more":
                result=pd.DataFrame(product.objects.filter(price__gte=int(key)))
    return render(request,"dispro.html")