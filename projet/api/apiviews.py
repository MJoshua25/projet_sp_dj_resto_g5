from rest_framework import viewsets, filters
from .models import *
from .serializers import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
    
class MessageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class NewsletterViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    
class PresentationViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    
class SocialViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class PersonnelViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class PosteViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

class MenuViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class PlatViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class TableViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class InfoUserViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer

class TemoignageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Temoignage.objects.all()
    serializer_class = TemoignageSerializer
