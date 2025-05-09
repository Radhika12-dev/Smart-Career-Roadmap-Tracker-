from django.db import models
from django.conf import settings

class RoadMap(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='roadmap')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models .BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
