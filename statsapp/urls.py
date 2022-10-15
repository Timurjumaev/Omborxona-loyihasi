from django.urls import path

from .views import StatistikaView

urlpatterns = [
    path('stats/', StatistikaView.as_view())
]