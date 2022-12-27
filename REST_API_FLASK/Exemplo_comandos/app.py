from flask import Flask,jsonify, request
import json 


app = Flask(__name__)


@app.route('/<int:id>') #esse int é a tipagem
def pessoas(id):
    return jsonify({'id':id,'nome':'Emmanuel','profissao': 'professor'})

# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1,valor2):
#     return jsonify({'soma':valor1+valor2})

# outra forma de implementar o código comentado acima
@app.route('/soma', methods=['POST','GET'])
def soma():

    if request.method=='POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        print(dados)
        return jsonify({'soma':total})
    elif request.method=='GET':
        total = 10+40
        return jsonify({'soma_x_2':2*total})
    



if __name__=="__main__":
    app.run(debug=True)
    