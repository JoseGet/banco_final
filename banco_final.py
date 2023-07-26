saldo = 0.0
tot_saques = 1
extrato = ""
numero_da_conta = 1
numero_da_agencia = "0001"

usuarios = {}
agencias = {}

menu = """

Olá! Seja bem-vindo ao Menu de atendimento do Banco Cash

Digite as seguintes opções que desejar:

1 - Operação de Depósito

2 - Operação de Saque

3 - Operação de Extrato

4 - Operação de Criação de Usuário

5 - Operação de Criação de Conta Corrente

6 - Sair


"""

def criar_conta_corrente(nC,nA, usu):
     
    chave = input("Digite o CPF do usuário que deseja vincular a conta: ")

    u = usu.get(chave)

    if(u == None):
         print("Usuário não encontrado.")
    else:
         agencias.update({nC : {"numero da agencia": nA, "cpf": u}})
         print("Conta Corrente criada! Operação finalizada.")


def criar_usuario():
     
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço no formado: logradouro, numero - bairro - cidade/sigla do estado: ")
    cpf = input("Digite seu CPF: ")

    if usuarios == {}:
        usuarios.update({cpf : {"nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}})
        print("Usuário cadastrado! Operação finalizada.")


    else:

        if cpf in usuarios:
            print("Este usuário já foi cadastrado.")

        else:
            usuarios.update({cpf : {"nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}})
            print("Usuário cadastrado! Operação finalizada.")


def funcao_extrato(saldo, /, extrato_final):
     
     if(extrato_final == ""):
            print("Não foram realizadas movimentações.")
     else:
            print(extrato_final)
            print(f"\nO saldo atual da sua conta é de R${saldo:.2f}")




def funcao_deposito(saldo_deposito, extrato_deposito):

     print("Digite o valor a ser depositado:")

     valor_deposito = float(input())

     if (valor_deposito <= 0):
         print("Impossível depositar valores negativos ou iguais a zero.")

     else :
            saldo_deposito += valor_deposito
            extrato_deposito = extrato_deposito + f"Depósito de R${valor_deposito:.2f} foi realizado\n"
            print("Operação efetuada!\n")
            return saldo_deposito, extrato_deposito



    

def funcao_saque(*,saldo_saque, extrato_saque, tot_saques):

    if tot_saques <= 3:

            valor_saque = float(input("Digite o valor a ser sacado: \n"))

            if(valor_saque > 500):

                print("Impossível realizar saques superiores a R$500,00")

            else:

                if(valor_saque > saldo_saque):

                    print("Impossível sacar este valor, por favor verifique seu extrato.")

                else:

                    saldo_saque -= valor_saque
                    extrato_saque = extrato_saque + f"Saque de R${valor_saque:.2f} foi realizado\n"
                    tot_saques += 1
                    print("Operação efetuada\n")
                    return saldo_saque, extrato_saque, tot_saques
    else:
         print("Limite de 3 saques diários atingido.")

    return saldo_saque, extrato_saque, tot_saques

while True:

    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato =  funcao_deposito(saldo, extrato)

    elif opcao == 2:
        saldo, extrato, tot_saques = funcao_saque(saldo_saque=saldo, extrato_saque=extrato, tot_saques=tot_saques)

    elif opcao == 3:
        funcao_extrato(saldo, extrato_final=extrato)

    elif opcao == 4:
        criar_usuario()

    elif opcao == 5:
         criar_conta_corrente(numero_da_conta,numero_da_agencia, usuarios)
         numero_da_conta += 1

    elif opcao == 6:

       print("Consulta finalizada, obrigado por ser nosso cliente! Até mais!") 
       break

    else:
        print("Opção inválida, por favor digite novamente.")

