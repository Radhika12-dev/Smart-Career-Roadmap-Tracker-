from rest_framework import serializers
from .models import *

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['id', 'user', 'roadmap', 'content', 'created_at']
        read_only_fields = ['id','user','created_at']