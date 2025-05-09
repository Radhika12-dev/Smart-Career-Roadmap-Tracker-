from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class RoadMapCreateView(generics.ListCreateAPIView):
    serializer_class = RoadMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoadMap.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class RoadMapDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoadMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoadMap.objects.filter(user = self.request.user)
    
    def put(self, request, *args, **kwargs):
        isinstance = self.get_object()
        serializer = self.get_serializer(isinstance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        isinstance = self.get_object()
        isinstance.delete()
        return Response({'message':'RoadMap item is deleted'}, status= status.HTTP_204_NO_CONTENT)