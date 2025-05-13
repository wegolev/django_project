#from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def material_list(request):
    return JsonResponse({'message': 'Materials API works!'})