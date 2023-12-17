from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
   """Exibindo todos os clientes"""
   class Meta:
      model = Cliente
      fields = '__all__'
