from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def mission(request):
    return render(request, 'mission.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'base.html', {})
