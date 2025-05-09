from django.db import models
from django.conf import settings
from roadmap.models import RoadMap
# Create your models here.

class Tip(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roadmap = models.ForeignKey(RoadMap, on_delete=models.CASCADE, related_name='tips')
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tips by {self.user.email} for {self.roadmap.title}"
