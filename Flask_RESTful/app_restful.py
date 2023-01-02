from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
        {
        'id':'0',
        'nome': 'Fulano',
        'habilidades':['python','flask']
        },
        {
        'id':'1',
        'nome': 'Ciclano',
        'habilidades':['c', 'c#','java']
        },
        {
        'id':'2',
        'nome': 'Beltrano',
        'habilidades':['php', 'python','html']
        }
                   
]



class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response=desenvolvedores[id]    
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem': mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido! Procure o administrador da API'
            response = {'status':'erro','mensagem': mensagem}
        return (response)
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self,id):
        desenvolvedores.pop(id)
        return ({'status': 'Sucesso','messagem': 'Registro Excluído!'})
    
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id']=posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])
    


api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades,'/habilidades/')

if __name__ == "__main__":
    app.run(debug=True)