from rest_framework import serializers
from seguranca.models import *

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ZonasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zonas
        fields = '__all__'

class OcorrenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

