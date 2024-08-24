from rest_framework import serializers
from .models import EstadoModel

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoModel
        fields = '__all__'
