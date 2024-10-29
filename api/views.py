from .serializer import CommandSerializer
from rest_framework import generics
from commands.models import Command
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.permissions import IsAuthenticated
from .throttle import UserBaseRateThrottle
class CommanAPI(ViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserBaseRateThrottle]
    def list(self, request):
        queryset = Command.objects.all()
        serializer = CommandSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CommandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"{serializer.data['name']}"}, status=status.HTTP_201_CREATED)
        return Response( {"message": "Something went wrong"} ,serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        try:
            queryset = Command.objects.get(pk=pk)
        except Command.DoesNotExist:
            return Response({"message": f"Command with ({pk}) not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommandSerializer(queryset)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        queryset = Command.objects.all()
        command = get_object_or_404(queryset, pk=pk)
        command.delete()
        # send success response to show successful deletion
        return Response({'message': 'Command deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Command.objects.all()
        command = get_object_or_404(queryset, pk=pk)
        serializer = CommandSerializer(command, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Command updated successfully{serializer.data}"}, status=status.HTTP_200_OK)
        return Response({"message": "Something went wrong"}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
