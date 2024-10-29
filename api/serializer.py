from rest_framework.serializers import ModelSerializer
from commands.models import Command

class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'

