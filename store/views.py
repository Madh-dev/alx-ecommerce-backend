from django.shortcuts import render

# store/views.py
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Store API Home"})
