from django.urls import path, include
from .viewsets import CidadeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cidades', CidadeViewSet, basename='cidade')

urlpatterns = [
    path('cidade/', include(router.urls))
]