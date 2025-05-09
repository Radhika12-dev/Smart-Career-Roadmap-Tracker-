from django.urls import path
from .views import *

urlpatterns = [
    path('', TipListCreateView.as_view(), name='tip-list-create'),
    path('<int:pk>/', TipDetailView.as_view(), name='tip-detail')
]
