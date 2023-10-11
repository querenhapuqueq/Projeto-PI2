from rest_framework import viewsets
from seguranca.api import serializers
from seguranca.models import *

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializers
    queryset = Usuario.objects.all()

class ZonasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ZonasSerializers
    queryset = Zonas.objects.all()

class OcorrenciaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OcorrenciaSerializers
    queryset = Ocorrencia.objects.all()
