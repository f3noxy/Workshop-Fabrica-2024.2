from django.urls import path, include
from .viewsets import EstadoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'estados', EstadoViewSet, basename='estado')

urlpatterns = [
    path('estado/', include(router.urls))
]