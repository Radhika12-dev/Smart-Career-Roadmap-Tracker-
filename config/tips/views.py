from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import *
from .serializers import TipSerializer
from rest_framework.response import Response
from .utils import *
import openai

class TipListCreateView(generics.ListCreateAPIView):
    serializer_class = TipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tip.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        roadmap = serializer.validated_data.get('roadmap')
        context = serializer.validated_data.get('context', '')

        personalized_tip = generate_personalized_tips(context, roadmap.title)
        serializer.save(user = self.request.user, context=personalized_tip)

class TipDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tip.objects.filter(user = self.request.user)
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message":"Invalid Data"}, status =status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
