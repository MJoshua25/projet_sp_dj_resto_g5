from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'pages/menu.html')

def special(request):
    return render(request, 'pages/special.html')