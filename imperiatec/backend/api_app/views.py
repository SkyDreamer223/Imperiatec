from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import User
from api_app.serializers import UserSerializer
from api_app.models import Arrivals
from api_app.serializers import ArrivalsSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ArrivalsViewSet(viewsets.ModelViewSet):
    queryset = Arrivals.objects.all()
    serializer_class = ArrivalsSerializer