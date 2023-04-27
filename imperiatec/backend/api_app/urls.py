from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from api_app.views import UserViewSet
from api_app.views import ArrivalsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'arrivals', ArrivalsViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
