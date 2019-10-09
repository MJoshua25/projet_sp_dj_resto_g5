from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from configuration.models import *
from contact.models import *
from entreprise.models import *
from menu.models import *
from reservation.models import *
from statistic.models import *
from temoignage.models import * 

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

class PresentationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class Social_entSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Social_ent
        fields = '__all__'


class PersonnelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    presonnel_Social = Social_entSerializer(many=True, required=False)
    class Meta:
        model = Personnel
        fields = '__all__'

class PosteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    poste_presonnel = PersonnelSerializer(many=True, required=False)
    class Meta:
        model = Poste
        fields = '__all__'

###################### SERIALIZERS DE MENU ######################

class MenuSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class PlatSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    menu_plat = MenuSerializer(many=True, required=False)
    class Meta:
        model = Plat
        fields = '__all__'


class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    menu_plat = PlatSerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    ingrediant_plat = PlatSerializer(many=True, required=False)
    class Meta:
        model = Ingredient
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

