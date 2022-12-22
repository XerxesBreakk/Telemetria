from django.urls import path
from . import views

urlpatterns = [
    path('lightStatus/',views.lightStatus,name="lightStatus"),
]
