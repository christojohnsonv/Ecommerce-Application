from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from product.models import category, product
from .models import User, order, order_details
from django.contrib.auth import logout,authenticate,login
from django.core.files.storage import FileSystemStorage
import datetime
import pandas as pd
from product.models import cart


def get_last_id(self):
    last_id=int(self.objects.order_by('id').last().id)
    return(last_id+1)



def Usignup(request):
    if request.method=="POST":
        fna=request.POST.get("first_name")
        lna=request.POST.get("last_name")
        em=request.POST.get("email")
        pw=request.POST.get("password")
        User.objects.create_user(first_name=fna,last_name=lna,email=em,password=pw)
        return redirect("ulogin")
    return render(request,"signup.html")


def Ulogin(request):
    if request.method=="POST":
        em=request.POST.get("email")
        pw=request.POST.get("password")
        user=authenticate(request,email=em,password=pw)
        if user:
            login(request,user)
            return redirect("disses")
        else:
            return redirect("ulogin")
    return render(request,"login.html")




def signout(request):
    logout(request)
    return redirect("ulogin")


def addusr(request):
    if request.method=="POST":
        cdate=datetime.datetime.now()
        fna=request.POST.get("fname")
        lna=request.POST.get("lname")
        em=request.POST.get("email")
        pw=request.POST.get("password")
        ph=request.POST.get("phone")
        gn=request.POST.get("gender")
        ad=request.POST.get("address")
        pc=request.POST.get('postcode')
        ct=request.POST.get('city')
        im=request.FILES['image']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        User.objects.create_user(first_name=fna,last_name=lna,email=em,password=pw,phone=ph,gender=gn,address=ad,image=fp,created_at=cdate,postcode=pc,city=ct)
    return render(request,"addusr.html")






def disusr(request):
    obj=User.objects.all()
    return render(request,"disusr.html",{"k":obj})


def updupw(request,userid):
    if request.method=="POST":
        npw=request.POST.get("newpassword")
        u=User.objects.get(id=userid)
        print(u)
        u.set_password(npw)
        u.save()
        return redirect("disusr")
    return render(request,"updupw.html",{'id':userid})


def updusr(request,userid):
    obj=User.objects.filter(id=userid).values()
    if request.method=="POST":
        fn=request.POST.get("first_name")
        ln=request.POST.get("last_name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        gn=request.POST.get("gender")
        ad=request.POST.get("address")
        obj.update(first_name=fn,last_name=ln,email=em,phone=ph,gender=gn,address=ad)
        return redirect("disusr")
    return render(request,"updusr.html",{'datas':obj[0],'id':userid})





def updupc(request,userid):
    obj=User.objects.filter(id=userid).values()
    if request.method=="POST":
        im=request.FILES['image']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        obj.update(image=fp)
        return redirect('disusr')
    return render(request,"updupc.html",{'id':userid})






# def updses(request,userid):
#     obj=User.objects.filter(id=userid).values()
#     if request.method=="POST":
#         npw=request.POST.get("newpassword")
#         u=User.objects.get(email=request.user.email)
#         u.set_password(npw)
#         u.save()
#         fn=request.POST.get("first_name")
#         ln=request.POST.get("last_name")
#         em=request.POST.get("email")
#         ph=request.POST.get("phone")
#         gn=request.POST.get("gender")
#         ad=request.POST.get("address")
#         im=request.FILES['image']
#         f=FileSystemStorage()
#         fp=f.save(im.name,im)
#         obj.update(first_name=fn,last_name=ln,email=em,phone=ph,gender=gn,address=ad,image=fp)
#         return redirect("disusr")
#     return render(request,"updses.html",{'datas':obj[0]})






def delusr(request,userid):
    obj=User.objects.get(id=userid)
    obj.delete()
    return redirect("disusr")







def disses(request):
    return render(request,"disses.html")








# Order functions
def addord(request):
    user=request.user.email
    prod=cart.objects.filter(user_id=user)
    ca=category.objects.all()
    sum=0
    for i in prod:
        sum=sum+int(i.total)

    usr=request.user.email
    car_pro=cart.objects.filter(user_id=usr)

    odat=datetime.datetime.now()
    usri=User.objects.get(id=request.user.id)
    deld=datetime.date.today() + datetime.timedelta(days=7)

    if request.method=="POST":
        pm=request.POST.get("paymentMethod")
        for i in car_pro:
            otot=i.total
            veni=i.product_id.vendor_id
            id_var=order.objects.create(order_date=odat,order_total=otot,customer_id=usri,delivery_date=deld,vendor_id=veni)
            proi=i.product_id
            proq=i.product_qty
            prop=i.product_id.price
            ordi=order.objects.get(id=id_var.id)
            order_details.objects.create(Product_id=proi,Product_quantity=proq,Product_Price=prop,order_id=ordi,Subtotal=otot,Payment_methos=pm,Paymrnt_status="Success")
            proinst=product.objects.get(id=proi.id)
            proqdif=(proinst.stock)-proq
            proinc=product.objects.filter(id=proi.id).values()
            proinc.update(stock=proqdif)

        car_pro.delete()
        return redirect("discart")
    return render(request,"usercheckout.html",{'pro':prod,'cat':ca,"subt":sum})


def disord(request):
    obj=order_details.objects.all()
    return render(request,"disord.html",{'datas':obj})



def userlogin(request):
    if request.method=="POST":
        em=request.POST.get("email")
        pw=request.POST.get("password")
        user=authenticate(request,email=em,password=pw)
        if user:
            login(request,user)
            return redirect("userhome")
        else:
            return render("userhome")
    return render(request,"auth-signin.html")




def usersignup(request):
    if request.method=="POST":
        fna=request.POST.get("first_name")
        lna=request.POST.get("last_name")
        em=request.POST.get("email")
        pw=request.POST.get("password")
        User.objects.create_user(first_name=fna,last_name=lna,email=em,password=pw)
        return redirect("userlogin")
    return render(request,"auth-signup.html")
   