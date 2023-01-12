from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    #usuario = request.user
    evento = Evento.objects.all() #filter(usuario = usuario)#all #get(id=1)
    dados = {'eventos': evento}
    return render(request,'agenda.html',dados)

# def index(request):
#     return redirect('/agenda')