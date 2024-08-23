from rest_framework import serializers
from .models import LivroModel

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroModel
        fields = '__all__'