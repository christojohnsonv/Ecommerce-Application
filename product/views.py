from os import path
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from vendor.models import vendor
from .models import cart, category, wishlist

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




def userhome(request):
    user_email=request.user.email
    car=cart.objects.filter(user_id=user_email)
    ca=category.objects.all()
    df=product.objects.filter(price__gte=100000)
    return render(request,"userhome.html",{'cat':ca,'pro':df,'cart':car})

def usershop(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'usershop.html',{'pro':prod,'cat':ca})

def usershopsearch(request):
    global catfilter
    prod=product.objects.all()
    ca=category.objects.all()
    if request.method=="POST":
        key=request.POST.get("searchkey")
    prod=product.objects.filter(product_description__contains=key)
    catfilter=prod
    return render(request,'usershop.html',{'pro':prod,'cat':ca})

def usershopfilter(request,catid):
    global catfilter
    catfilter=product.objects.all()
    ca=category.objects.all()
    temp=category.objects.get(id=catid)
    catfilter=product.objects.filter(pcategory__category_name=temp)
    prod=catfilter    
    return render(request,'usershop.html',{'pro':prod,'cat':ca})





def userpricefilter(request):
    global catfilter
    prod=catfilter
    ca=category.objects.all()
    if request.method=="POST":
        low=request.POST.get("low")
        high=request.POST.get("high")
        if low=="":
            if high=="":
                prod=catfilter
            else:
                prod=catfilter.filter(price__lte=high)
        else:
            if high=="":
                prod=catfilter.filter(price__gte=low)
            else:
                prod=catfilter.filter(price__gte=low,price__lte=high)
    catfilter=prod
    return render(request,'usershop.html',{'pro':prod,'cat':ca,"h":high,"l":low})






def usershopsort(request):
    prod=catfilter
    ca=category.objects.all()
    if request.method=="POST":
        key=request.POST.get("sortkey")
        if key=="":
            prod=catfilter
        elif key=="2":
            prod=prod.order_by('price')
            prod=prod.reverse()
        elif key=="3":
            prod=prod.order_by('price')
    return render(request,'usershop.html',{'pro':prod,'cat':ca})







def add2cart(request,proid):
    prod=product.objects.all()
    prod_var=product.objects.get(id=proid)
    ca=category.objects.all()
    user_mail=request.user.email
    tot=prod_var.price
    cart.objects.create(product_id=prod_var,product_qty=1,user_id=user_mail,total=tot)
    return redirect("usershop")
    return render(request,'usercart.html',{'pro':prod,'cat':ca})

def discart(request):
    user=request.user.email
    prod=cart.objects.filter(user_id=user)
    
    ca=category.objects.all()
    sum=0
    for i in prod:
        sum=sum+int(i.product_id.price)
    
    return render(request,'usercart.html',{'pro':prod,'cat':ca,"subt":sum})


def userwish(request,proid):
    prod=product.objects.all()
    prod_var=product.objects.get(id=proid)
    ca=category.objects.all()
    user_mail=request.user.email
    wishlist.objects.create(product_id=prod_var,user_id=user_mail)
    return redirect("diswish")
    return render(request,'userwishlist.html',{'pro':prod,'cat':ca})





def diswish(request):
    user=request.user.email
    prod=wishlist.objects.filter(user_id=user)
    
    ca=category.objects.all()
    return render(request,'userwishlist.html',{'pro':prod,'cat':ca,"subt":sum})





def userprofiledis(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'usershop.html',{'pro':prod,'cat':ca})

def userprofileupd(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'usermy-account.html',{'pro':prod,'cat':ca})

def userpasswordupd(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'usermy-account.html',{'pro':prod,'cat':ca})

def userabout(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'userabout.html',{'pro':prod,'cat':ca})

def userservice(request):
    prod=product.objects.all()
    ca=category.objects.all()
    
    return render(request,'userservice.html',{'pro':prod,'cat':ca})




def usercheckout(request):
    prod=product.objects.all()
    ca=category.objects.all()
    return render(request,'usercheckout.html',{'pro':prod,'cat':ca})






def delcart(request,car_id):
    obj=cart.objects.get(id=car_id)
    obj.delete()
    return redirect("discart")



def updcart(request,cid):
    obj=cart.objects.filter(id=cid).values()
    v=cart.objects.get(id=cid)
    if request.method=="POST":
        qty=request.POST.get("qty")
    obj.update(product_qty=qty,total=int(qty)*int(v.product_id.price))
    return redirect("discart")

