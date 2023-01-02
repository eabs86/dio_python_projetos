from flask import Flask, jsonify,request
import json
app = Flask(__name__)


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

#devolve um desenvolvedor pelo ID, faz alteração e deleta
@app.route('/dev/<int:id>',methods=['GET','PUT','DELETE'])
def lista_dev(id):
    
    if request.method == 'GET':
        try:
            response=desenvolvedores[id]
            
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem': mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido! Procure o administrador da API'
            response = {'status':'erro','mensagem': mensagem}
        return jsonify(response)
        # desenvolvedor = desenvolvedores[id]
        # return jsonify(desenvolvedor)
    elif request.method=='PUT':
        dados=json.loads(request.data)
        desenvolvedores[id]=dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id) #deleta o último registro
        return jsonify({'status': 'Sucesso','messagem': 'Registro Excluído!'})

#lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])

def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id']=posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method=='GET':
        return jsonify(desenvolvedores)
                
if __name__ == "__main__":
    app.run(debug=True)
