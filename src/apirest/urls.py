from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apirest.views import CocktailViewSet

router = DefaultRouter()
router.register(r'cocktails', CocktailViewSet)

urlpatterns = [
    url(r'^v1/', include((router.urls, 'apirest'), namespace='v1')),
]
