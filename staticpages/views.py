from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'staticpages/index.html')

def about(request):
    return render(request, 'staticpages/about.html')