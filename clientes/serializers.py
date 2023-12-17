from rest_framework import serializers
from .models import Cliente
from .validators import *

class ClienteSerializer(serializers.ModelSerializer):
   """Exibindo todos os clientes"""
   class Meta:
      model = Cliente
      fields = '__all__'
   
   def validate(self, data):
      if not cpf_valido(data['cpf']):
         raise serializers.ValidationError({'cpf':"O campo CPF deve ter 11 dígitos"})
      if not nome_valido(data['nome']):
         raise serializers.ValidationError({'nome': "O campo nome não pode ter números"})
      if not rg_valido(data['rg']):
         raise serializers.ValidationError({'rg': "O campo RG deve ter 9 dígitos"})
      if celular_valido(data['celular']):
         raise serializers.ValidationError({'celular': "O celular de ver 11 dígitos"})
      return data

   
   """ def validate_cpf(self, cpf):
      if len(cpf) != 11:
         raise serializers.ValidationError("O CPF deve ter 11 dígitos")
      return cpf

   def validate_nome(self, nome):
      if not nome.isalpha():
         raise serializers.ValidationError("Não inclua número no campo nome")
      return nome

   def validate_rg(self, rg):
      if len(rg) != 9:
         raise serializers.ValidationError("O RG deve ter 9 dígitos")
      return rg

   def validate_celular(self, celular):
      if len(celular) < 11:
         raise serializers.ValidationError("O celular de ver 11 dígitos")
      return celular """