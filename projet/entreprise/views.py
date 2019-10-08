from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def teams(request):
    return render(request, 'pages/teams.html')

def about(request):
    return render(request, 'pages/about.html')