from django.shortcuts import render
from configuration.models import *

# Create your views here.
def reservation(request):
       
    hour = WorkingHour.objects.filter(statut=True)
    reservation_form = ReserveConfiguration.objects.filter(statut=True)
    

    data = {
        
    
        'hour':hour,
        'form':reservation_form,
        
 
    }

    
    template_name = 'pages/reservation.html'
    
    
    
    return render(request,template_name, data)