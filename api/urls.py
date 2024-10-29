from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

router.register(r'commands', CommanAPI, basename='commands_api')


urlpatterns = [
    path('', include(router.urls))
]