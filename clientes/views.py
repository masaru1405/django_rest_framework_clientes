from rest_framework import viewsets

from .serializers import ClienteSerializer
from .models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
   """Listando todos os clientes"""
   queryset = Cliente.objects.all()
   serializer_class = ClienteSerializer