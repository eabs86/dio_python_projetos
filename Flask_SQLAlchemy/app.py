from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


# USUARIOS = {
#     'fulano': '321',
#     'beltrano':'321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     print('validando usuario...')
#     print(USUARIOS.get(login)==senha)
#     if not(login, senha):
#         return False
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    print('validando usuario...')
    if not(login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()
    

class Pessoa(Resource):
    
    @auth.login_required
    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response={
                'status':'error',
                'mensagem': 'Pessoa nao encontrada!'
            }
        return response

    def put(self, nome):
        
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = json.loads(request.data)
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade': pessoa.idade
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
         
        return {'status':'sucesso', 'mensagem' : mensagem}
    
class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all() #só fazer isso quando a tabela tiver poucos registros. NÃO FAZER QUANDO O BANCO TEM MUITOS DADOS
        response = [{'id':i.id,'nome':i.nome,'idade':i.idade} for i in pessoas]
        return response
    
    def post(self):
        dados = json.loads(request.data)
        pessoa = Pessoas(nome=dados['nome'],idade = dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade          
        }
        return response

class ListaAtividades(Resource):
    
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id,'nome':i.nome,'pessoa':i.pessoa.nome} for i in atividades]
        return response
    
    def post(self):
        dados = json.loads(request.data)
        pessoa = Pessoas.query.filter_by(nome = dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'],pessoa=pessoa)
        atividade.save()
        
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response
api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoa/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == "__main__":
    app.run(debug=True)