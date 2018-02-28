from rest_framework import viewsets

from apirest.models import Cocktail
from apirest.serializers import CocktailSerializer


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.order_by('name')
    serializer_class = CocktailSerializer
