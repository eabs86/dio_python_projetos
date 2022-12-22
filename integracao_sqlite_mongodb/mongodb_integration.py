import pymongo as pyM
import datetime
import pprint
client = pyM.MongoClient("mongodb+srv://usuario:senha@cluster1.msjr9x6.mongodb.net/?retryWrites=true&w=majority")

db = client.test

post = {
    "author": "Cliente1 Fulano",
    "address": "cliente1@mail.com",
    "cpf": "00000000001",
    "tipo_conta": "conta corrente",
    "numero_conta": 1000,
    "agência": '0001',
    "saldo": 3000,
    "tags": ["cliente1", "fulano", "corrente", "pf", "adulto", "masculino"],
    "date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())


# recuperar informações
print("\n Recuperando informação de cadastro:\n")
print(db.posts.find_one())
pprint.pprint(db.posts.find_one())


# bulk insert
new_posts = [{
    "author": "Cliente2 Beltrano",
    "address": "cliente2@mail.com",
    "cpf": "00000000002",
    "tipo_conta": "conta corrente",
    "numero_conta": 1001,
    "agência": '0001',
    "saldo": 2000,
    "tags": ["cliente2", "beltrano", "corrente", "pf", "adulto", "feminino"],
    "date": datetime.datetime.utcnow()
},
    {
    "author": "Cliente3 Ciclano",
    "address": "cliente3@mail.com",
    "cpf": "00000000003",
    "tipo_conta": "conta corrente",
    "numero_conta": 1002,
    "agência": '0001',
    "saldo": 10000,
    "tags": ["cliente3", "ciclano", "corrente", "pj", "empresa", "adulto", "masculino"],
    "date": datetime.datetime.utcnow()
},
    {
    "author": "Cliente4 Fulano",
    "address": "cliente4@mail.com",
    "cpf": "00000000004",
    "tipo_conta": "poupanca",
    "numero_conta": 9001,
    "agência": '0001',
    "saldo": 500,
    "tags": ["cliente4", "fulano", "poupanca", "pf", "crianca", "feminino"],
    "date": datetime.datetime.utcnow()
}]


result = posts.insert_many(new_posts)
print("\n Ids nos novos cadastrados:\n")
print(result.inserted_ids)

# fazendo uma busca pelos clientes da mesma família
print("\n Clientes da mesma família:\n")
pprint.pprint(db.posts.find_one({"tags": "fulano"}))

# Imprimindo os cadastros que estão na coleção
print("\n Documentos presentes na coleção Posts")
for post in posts.find():
    pprint.pprint(post)

