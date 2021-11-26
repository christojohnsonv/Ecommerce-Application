from django.db import models
from django.db.models import fields
from django.http.response import FileResponse
from rest_framework import serializers
from .models import User, delivery_agent, order




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = delivery_agent
        fields = '__all__'
