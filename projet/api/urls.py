from rest_framework.routers import DefaultRouter
from .apiviews import *

router = DefaultRouter()
router.register('message', MessageViewSet, base_name='message')
router.register('newletters', NewsletterViewSet, base_name='newletters')
router.register('presentation', PresentationViewSet, base_name='presentation')
router.register('social', Social_entViewSet, base_name='social')
router.register('personnel', PersonnelViewSet, base_name='personnel')
router.register('poste', PosteViewSet, base_name='poste')
router.register('menu', MenuViewSet, base_name='menu')
router.register('plat', PlatViewSet, base_name='plat')
router.register('categorie', CategoryViewSet, base_name='categorie')
router.register('ingredient', IngredientViewSet, base_name='ingredient')
router.register('reservation', ReservationViewSet, base_name='reservation')
router.register('table', TableViewSet, base_name='table')
router.register('infouser', InfoUserViewSet, base_name='infouser')
router.register('temoignage', TemoignageViewSet, base_name='temoignage')

urlpatterns = [
    # ...
]

urlpatterns += router.urls