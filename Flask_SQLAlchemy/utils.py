from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Ciclano', idade='20')
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


if __name__ == "__main__":
    # insere_pessoas()
    consulta()
    # altera()
    # exclui()