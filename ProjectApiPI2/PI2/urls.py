from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from seguranca.api import viewsets

route = routers.DefaultRouter()
route.register(r'usuario/', viewsets.UsuarioViewSet, basename='Usuário')
route.register(r'zonas/', viewsets.ZonasViewSet, basename='Zonas')
route.register(r'ocorrencia/', viewsets.OcorrenciaViewSet, basename='Ocorrências')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include(route.urls)),
]
