from rest_framework import serializers
from .models import *

class RoadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMap
        fields = ['id', 'title', 'description', 'completed', 'created_at']