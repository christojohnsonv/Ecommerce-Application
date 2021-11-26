from os import name
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
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




