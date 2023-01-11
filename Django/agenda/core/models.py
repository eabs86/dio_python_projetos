from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) # sempre que for criado o registro a hora atual será inserida
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

'''
Comandos para criar o arquivo de migração:

python manage.py makemigrations core 

python manage.py sqlmigrate core 0001 # esse aqui é para criar o modelo a partir do arquivo 0001

python manage.py migrate core 0001

'''
