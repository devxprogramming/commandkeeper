from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from commands.models import Command
from .serializer import CommandSerializer
from .throttle import UserBaseRateThrottle


class CommandAPI(viewsets.ModelViewSet):
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserBaseRateThrottle]

    def get_queryset(self):
        return Command.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = get_object_or_404(self.get_queryset(), pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), pk=kwargs.get('pk'))
        self.perform_destroy(instance)
        return Response({'message': 'Command deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
