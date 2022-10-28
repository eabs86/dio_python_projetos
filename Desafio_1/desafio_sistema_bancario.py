"""
Desafio - Sistema Bancário - DIO

Autor: Emmanuel Andrade
Data: 28/10/2022


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
numero_saques = 3
LIMITE_SAQUES = 3
contador_saque=0
saques_acumulados = 0
contador_deposito=0
depositos_acumulados =0

while True:  #laço infinito
    
    opcao = input(menu) #faz a leitura do comando de entrada
    
    
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Quanto você deseja depositar?:"))
        if (deposito>0): #verifica se o valor a ser depositado é positivo
            saldo= saldo+deposito
            contador_deposito +=1
            depositos_acumulados=depositos_acumulados+deposito
            extrato = extrato + f"\nDepósito nº{contador_deposito}: + R$ {deposito:.2f}" #faz a adição da string ao texto que irá aparecer no extrato
        else:   #se o valor a ser depositado for negativo
            print("Valor de saque inválido. Tente novamente!")
        
        
    elif opcao == "s":
        print("Saque")
        saque = float((input("Quanto você deseja sacar?:")))
        
        if (saldo<saque): #verifica se há saldo
            print("Saldo insuficiente!")
        elif(saldo>saque): #caso haja saldo, prossegue
            contador_saque +=1  #contador de saque. O limite é de 3 saques
            if(saque>limite): #se o saque for acima do limite diário de R$500,00
                print(f"Saque acima de R$ {limite:.2f} não permitido")
            elif(saque<limite): #se for menor que o limite diário, prossegue.
                if(contador_saque>numero_saques): #verifica se já atingiu a quantidade de saques diários.
                    print("\nLimite de saques diário atingido! Não é possível realizar mais de 3 saques ao dia!")
                else:
                    print("\nSaque realizado com sucesso!")
                    saques_acumulados = saques_acumulados+saque
                    extrato = extrato + f"\nSaque nº{contador_saque}: - R$ {saque:.2f}" #faz a adição da string ao texto que irá aparecer no extrato
                    saldo = saldo-saque
        
        
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