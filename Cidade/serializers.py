from rest_framework import serializers
from .models import CidadeModel

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CidadeModel
        fields = '__all__'