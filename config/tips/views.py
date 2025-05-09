from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import *
from .serializers import TipSerializer
from rest_framework.response import Response

class TipListCreateView(generics.ListCreateAPIView):
    serializer_class = TipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tip.objects.filter(user=self.request.user)
    
    def perform_create(self,serailizer):
        serailizer.save(user=self.request.user)

class TipDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tip.objects.filter(user = self.request.user)
    
    def put(self, request, *args, **kwargs):
        isinstance = self.get_object()
        serializer = self.get_serializer(isinstance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message":"Invalid Data"}, status =status.HTTP_400_BAD_REQUEST)


