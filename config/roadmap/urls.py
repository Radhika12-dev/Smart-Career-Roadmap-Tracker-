from django.urls import path
from .views import *

urlpatterns = [
    path('', RoadMapCreateView.as_view(), name='roadmap-list-create'),
    path('<int:pk>/', RoadMapDetailView.as_view(), name='roadmap-detail'),
]
