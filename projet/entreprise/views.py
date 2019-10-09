from django.shortcuts import render
from configuration.models import *
# Create your views here.



def about(request):
    about = About.objects.filter(statut=True)
    hour = WorkingHour.objects.filter(statut=True)

    data = {
   
        'hour':hour,
        'about':about,
      
    }

    template_name = 'pages/about.html'
 
    return render(request,template_name, data)
def teams(request):
       
    hour = WorkingHour.objects.filter(statut=True)

    data = {
   
        'hour':hour,
      
    }

    template_name = 'pages/teams.html'
  
    return render(request,template_name, data)