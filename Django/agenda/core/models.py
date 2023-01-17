from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
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
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%m')
    def get_data_input_evento(self): #função importante para colocar a data no padrão queo datetime-local entende
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False


'''
Comandos para criar o arquivo de migração:

python manage.py makemigrations core 

python manage.py sqlmigrate core 0001 # esse aqui é para criar o modelo a partir do arquivo 0001

python manage.py migrate core 0001

'''
