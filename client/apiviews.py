from os import name
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import *
from .models import User, order,delivery_agent


@api_view()
def disusrrest(request):
    v = User.objects.all()
    s = UserSerializer(v,many=True)
    return Response(s.data)

@api_view()
def disordrest(request):
    v = order.objects.all()
    s = OrderSerializer(v,many=True)
    return Response(s.data)





@api_view(['POST'])
def adddela(request):
    if request.method=="POST":
        na=request.data.get('name')
        pl=request.data.get('place')
        u=delivery_agent.objects.create(dname=na,dplace=pl)
        
        obj=delivery_agent.objects.filter(id=u.id)
        res=AgentSerializer(obj,many=True)
        return Response(res.data)
    return Response("fill form")

@api_view()
def disdela(request):
    v = delivery_agent.objects.all()
    s = AgentSerializer(v,many=True)
    return Response(s.data)

@api_view(['GET','PUT'])
def upddela(request,userid):
    u=delivery_agent.objects.filter(id=userid)
    if request.method=="PUT":
        na=request.data.get("name")
        pl=request.data.get("place")
        u.update(dname=na,dplace=pl)
        
        dis=delivery_agent.objects.filter(id=userid)
        ser=AgentSerializer(dis,many=True)
        return Response(ser.data)
    return Response("Please fill the form")
    



