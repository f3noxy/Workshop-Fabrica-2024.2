from rest_framework import viewsets
from .models import CidadeModel
from .serializers import CidadeSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = CidadeModel.objects.all()
    serializer_class = CidadeSerializer