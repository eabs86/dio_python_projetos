"""
Desafio - Sistema Bancário - DIO

Autor: Emmanuel Andrade
Data: 28/10/2022

Versão 2:
- Modularização
    - Utilização de funções
- Novas funcionalidades

"""


#Dicionário do MENU
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


====> Digite sua opção: """


#Declaração das variáveis e constantes
saldo = 1000
limite = 500
extrato=""
numero_saques = 0
LIMITE_SAQUES = 3
contador_saque=0
saques_acumulados = 0
contador_deposito=0
depositos_acumulados =0
lista_usuarios=[]
nro_contas=[]


def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    if (saldo<valor): #verifica se há saldo
        print("Saldo insuficiente!")
    elif(saldo>valor): #caso haja saldo, prossegue
        numero_saques+=1  #contador de saque. O limite é de 3 saques
        if(valor>limite): #se o saque for acima do limite diário de R$500,00
            print(f"Saque acima de R$ {limite:.2f} não permitido")
        elif(valor<limite): #se for menor que o limite diário, prossegue.
            if(numero_saques>limite_saques): #verifica se já atingiu a quantidade de saques diários.
                print("\nLimite de saques diário atingido! Não é possível realizar mais de 3 saques ao dia!")
            else:
                
                global saques_acumulados
                saques_acumulados +=valor
                print(f"\nSaque de R${valor:.2f} realizado com sucesso!")
                extrato = extrato + f"\nSaque nº{numero_saques}: - R$ {valor:.2f}" #faz a adição da string ao texto que irá aparecer no extrato

                saldo = saldo-valor
                
    return saldo,extrato

def depositar(saldo,valor,extrato,/):
    saldo= saldo+valor
    global contador_deposito
    contador_deposito+=1
    extrato = extrato + f"\nDepósito nº{contador_deposito}: + R$ {valor:.2f}" #faz a adição da string ao texto que irá aparecer no extrato   
    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!") 
    
    return saldo,extrato

def print_extrato(saldo,/,*,extrato):
    
    return extrato

def criar_usuario(nome="",data_nascimento="DD/MM/AAAA",cpf=1234567890,endereco="logradouro, nro - bairro - cidade/sigla estado"):
    #data de nascimento no formato: DD/MM/AAAA
    #endereço no formato: logradouro, nro - bairro - cidade/sigla estado
    check_cpf = cpf in lista_usuarios
    if check_cpf==True:
        print("Usuário Já cadastrado!")
    else:
        lista_usuarios.append(cpf)
    
    return check_cpf

def criar_conta(agencia="0001",nro_conta=0,usuario=1234567890 ):
    qtdade_contas=len(nro_contas)
    nova_conta=qtdade_contas+1
    return nova_conta

def listar_usuarios():
    print(listar_usuarios)
    
while True:  #laço infinito
    
    opcao = input(menu) #faz a leitura do comando de entrada
    
    
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Quanto você deseja depositar?:"))
        if (deposito>0): #verifica se o valor a ser depositado é positivo
            saldo,extrato=depositar(saldo,deposito,extrato)
            depositos_acumulados=depositos_acumulados+deposito
        else:   #se o valor a ser depositado for negativo
            print("Valor de saque inválido. Tente novamente!")
        
        
    elif opcao == "s":
        print("Saque")
        saque = float((input("Quanto você deseja sacar?:")))
        saldo,extrato = sacar(saldo=saldo,valor=saque,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques =LIMITE_SAQUES)
        
        
        
    elif opcao == "e":
        print("########## Extrato ########## ") #mostra o extrato completo com os saques e depósitos.
        extrato = extrato + f"""\n 
\n Valor total de saques:    - R$ {saques_acumulados:.2f}
\n Valor total de depositos: + R$ {depositos_acumulados:.2f}
\n __________________________________________________________        
        
   Seu saldo é de:             R$ {saldo:6.2f}"""
        
        print(extrato)
        
        
    elif opcao == "q":
        print("\n\nEncerrando...\n O Banco MR agradece a sua preferência!\n\n")
        break
    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada")