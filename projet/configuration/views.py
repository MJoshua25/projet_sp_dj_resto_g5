from django.shortcuts import render
from .models import *
import datetime

# Create your views here.


def home(request):
    hour = WorkingHour.objects.filter(statut=True)
    data = {
        'hour':hour,
    }

    template_name = 'pages/index.html'
    return render(request,template_name, data)

# def open_hour(request, table):
#     def __str__(self):
        
        
        
#         datahour={
            
#         }
        
        
        
#         jour = datetime.datetime.now()
#         jour =jour.strftime("%a")
#         if (jour == "Mon"):
#             heure = self.table.objects.filter(jour='lundi')
#             for heur in heure:
#                 jour =heur.jour
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         elif (jour == "Tue"):
#             heure = self.table.objects.filter(jour='mardi')
#             for heur in heure:
#                 jour =heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         elif (jour == "Wed"):
#             heure = self.table.objects.filter(jour ='mercredi')
#             for heur in heure:
                
#                 jour = heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#                 print("heure" , close)
#         elif (jour == "Thu"):
#             heure = self.table.objects.filter(jour = 'jeudi')
#             for heur in heure:
#                 jour =heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         elif (jour == "Fri"):
#             heure = self.table.objects.filter(jour='vendredi')
#             for heur in heure:
#                 jour =heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         elif (jour == "Sat"):
#             heure = self.table.objects.filter(jour='samedi')
#             for heur in heure:
#                 jour =heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         elif (jour == "Sun"):
#             heure = self.table.objects.filter(jour='dimanche')
#             for heur in heure:
#                 jour =heur.jour
                    
#                 heure = heur.start_hour
#                 close = heur.end_hour
#                 datahour={
#             'heure':heure,
#             'close':close,
#         }
#         return datahour