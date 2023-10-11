from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    UserID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=50, null=True)
    Sobrenome = models.CharField(max_length=30, null=True)
    Email = models.EmailField(max_length=255)
    Login = models.CharField(max_length=20, null=True)
    Senha = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return 'f{self.UserID} {Nome}'

class Zonas(models.Model):
    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    ZonaID = models.AutoField(primary_key=True)
    Nome_da_Zona = models.CharField(max_length=30, null=True)
    Tipo_Zona = models.CharField(max_length=50, null=True)
    Quantidade_Ocorrencias = models.IntegerField(null=True)
    Data_Ocorrencia = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self) -> str:
        return 'f{self.ZonaID} {Nome_da_Zona}'

class Ocorrencia(models.Model):
    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    OcorrenciaID = models.AutoField(primary_key=True)
    Tipo_Ocorrencia = models.CharField(max_length=50, null=True)
    Bairro = models.CharField(max_length=30,null=True)
    Longitude = models.CharField(max_length=30, null=True)
    Latitude = models.CharField(max_length=30, null=True)
    Data_Hora = models.DateTimeField(default=timezone.now, null=True)
    Descricao = models.TextField()
    Anexos = models.BooleanField()
    User_ID = models.ForeignKey(Usuario, on_delete=models.SET, null=True)
    Zonas_ID = models.ForeignKey(Zonas, on_delete=models.SET, null=True)

    def __str__(self) -> str:
        return 'f{self.OcorrenciaID} {Tipo_Ocorrencia}'

