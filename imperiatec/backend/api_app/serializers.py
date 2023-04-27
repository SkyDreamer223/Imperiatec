from rest_framework import serializers
from django.contrib.auth.models import User
from api_app.models import Arrivals


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class ArrivalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrivals
        fields = ('id', 'username', 'arrival_date', 'arrival_time')

