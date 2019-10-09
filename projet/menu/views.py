from django.shortcuts import render
from configuration.models import *
# Create your views here.
def menu(request):
    return render(request, 'pages/menu.html')

def menu(request):
       
    hour = WorkingHour.objects.filter(statut=True)

    data = {
   
        'hour':hour,
      
    }

    template_name = 'pages/menu.html'
    
    
    
    return render(request,template_name, data)


def special(request):
       
    hour = WorkingHour.objects.filter(statut=True)

    data = {
   
        'hour':hour,
      
    }

    template_name = 'pages/special.html'
    
    
    
    return render(request,template_name, data)
