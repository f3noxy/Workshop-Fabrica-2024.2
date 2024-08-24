from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CidadeModel
from .serializers import CidadeSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = CidadeModel.objects.all()
    serializer_class = CidadeSerializer