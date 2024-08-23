from django.urls import path, include
from .viewsets import LivroViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livro')

urlpatterns = [
    path('livro/', include(router.urls))
]