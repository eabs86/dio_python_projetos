from models import Pessoas, db_session,Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Beltrano', idade='21')
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    
def altera():
    pessoa = Pessoas.query.filter_by(nome='Ciclano').first()
    pessoa.idade = 21
    pessoa.save()
    
def exclui():
    pessoa = Pessoas.query.filter_by(nome = 'Ciclano').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    # insere_usuario('emmanuel','1234')
    # insere_usuario('andrade','4321')
    # insere_pessoas()
    # consulta()
    # altera()
    # exclui()
    consulta_todos_usuarios()