# store/urls.py
from django.urls import path
from . import views  # make sure you have views.py

urlpatterns = [
    # Example endpoint
    path('', views.home, name='home'),
]
