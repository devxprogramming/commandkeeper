from rest_framework.serializers import ModelSerializer
from commands.models import Command


class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = [
            'id',
            'cid',
            'user',
            'name',
            'description',
            'command',
            'tag',
            'level',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'cid', 'user', 'created_at', 'updated_at']
