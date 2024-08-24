from rest_framework import viewsets
from .models import EstadoModel
from .serializers import EstadoSerializer
import requests

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = EstadoModel.objects.all()
    serializer_class = EstadoSerializer

    def perform_create(self, serializer):
        nacao = serializer.validated_data.get('nacao')
        response = requests.get(f'https://restcountries.com/v3.1/name/{nacao}')

        if response.status_code == 200:
            nacao_data = response.json()
            serializer.save(infoNacao=nacao_data[0].get("timezones"))
        else:
            serializer.save()