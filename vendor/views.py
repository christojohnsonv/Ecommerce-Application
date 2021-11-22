from django.shortcuts import render

# Create your views here.

from .models import *

def addven(request):
    if request.method=="POST":
        na=request.POST.get("vname")
        em=request.POST.get("vemail")
        pw=request.POST.get("vpassword")
        br=request.POST.get("vbranch")
        ur=request.POST.get("vurl")
        ad=request.POST.get("vaddress")
        ph=request.POST.get("vphone")
        gs=request.POST.get("vgst")
        vendor.objects.create(vname=na,vemail=em,vpassword=pw,vbranch=br,vurl=ur,vaddress=ad,vphone=ph,vgst=gs)
    return render(request,"addven.html")

def disven(request):
    obj=vendor.objects.all()
    print(obj)
    return render(request,"disven.html",{"datas":obj})