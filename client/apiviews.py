from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import User, order


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