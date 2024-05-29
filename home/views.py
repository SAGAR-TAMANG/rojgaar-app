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