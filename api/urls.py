from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommandAPI

app_name = 'api'

router = DefaultRouter()
router.register(r'commands', CommandAPI, basename='commands_api')

urlpatterns = [
    path('', include(router.urls)),
]
