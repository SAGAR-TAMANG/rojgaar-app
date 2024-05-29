from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'sub/about.html')

def intro(request):
  return HttpResponse('')

def services(request):
  return render(request, 'sub/services.html')

def why(request):
  return render(request, 'sub/why.html')

import json, os
from django.http import JsonResponse
from django.conf import settings

def assetlinks_json(request):
    file_path = os.path.join(settings.STATIC_ROOT, '.well-known', 'assetlinks.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
