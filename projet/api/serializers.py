from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from configuration.models import *
from contact.models import *
from entreprise.models import *
from menu.models import *
from reservation.models import *
from statistic.models import *
from temoignage.models import * 
import simplejson as json

###################### SERIALIZERS DE CONTACT ######################

class MessageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NewsletterSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


###################### SERIALIZERS DE ENTREPRISE ######################
class PosteListingField(serializers.RelatedField):
    def to_representation(self, value):
        
                
               
               
        #duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return value.nom  
class PresentationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class SocialSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class PersonnelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    presonnel_Social = SocialSerializer(many=True, required=False)
    poste = PosteListingField( read_only=True,required=False)
    class Meta:
        model = Personnel
        fields = '__all__'

class PosteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    poste_presonnel = PersonnelSerializer(many=True, required=False)
    class Meta:
        model = Poste
        fields = '__all__'

###################### SERIALIZERS DE MENU ######################
class IngredientListingField(serializers.RelatedField):
    def to_representation(self, value):
        #duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return 'ingredient %d: %s ' % (value.id,value.nom  )
    
class PlatListingField(serializers.RelatedField):
    def to_representation(self, value):
        data ={'nom': value.nom,
                'id': value.id
               
               }
        #duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return data  
    #'%s ' % ( value.nom,)



class MenuSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    plats = PlatListingField(read_only=True ,many=True)
    
    class Meta:
        model = Menu
        fields = '__all__'

class PlatSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    menu_plat = MenuSerializer(many=True, required=False)
    ingredient = IngredientListingField(read_only=True ,many=True)
    
    class Meta:
        model = Plat
        fields = '__all__'



class IngredientSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    ingrediant_plat = PlatSerializer(many=True, required=False)
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    categorie_plat = PlatSerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = '__all__'



###################### SERIALIZERS DE RESERVATION ######################

class ReservationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TableSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    tables = ReservationSerializer(many=True, required=False)
    class Meta:
        model = Table
        fields = '__all__'


###################### SERIALIZERS DE STATISTIC ######################

class InfoUserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = '__all__'

###################### SERIALIZERS DE TEMOIGNAGE ######################

class TemoignageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'

