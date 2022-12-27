from flask import Flask, jsonify,request
import json
app = Flask(__name__)


desenvolvedores = [
        {'nome': 'Fulano',
         'habilidades':['python','flask']
        },
        {'nome': 'Ciclano',
        'habilidades':['c', 'c#','java']
        },
        {'nome': 'Beltrano',
        'habilidades':['php', 'python','html']
        }        
                   
]


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

if __name__ == "__main__":
    app.run(debug=True)
