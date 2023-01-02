from flask_restful import Resource

lista_habilidades = ['python','flask','java','php','html','c','c#']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def put(self):
        pass
    def post(self):
        pass
    def delete(self1):
        pass