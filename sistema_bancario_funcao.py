# SISTEMA BANCÁRIO COM FUNÇÕES EM PYTHON - DESAFIO DIO

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_conta = 0
limite_conta = 500
extrato_conta = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao_menu = input(menu)

    if opcao_menu == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo_conta += valor
            extrato_conta += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao_menu == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo_conta

        excedeu_limite = valor > limite_conta

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo_conta -= valor
            extrato_conta += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao_menu == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)
        print(f"\nSaldo atual: R$ {saldo_conta:.2f}")
        print(f"\nNumero de saques realizados: {numero_saques}")
        
        qtde_saques = LIMITE_SAQUES - numero_saques
        if qtde_saques == 1:
            print(f"Você ainda pode fazer {qtde_saques} saque.")        
        elif qtde_saques == 0:
            print(f"Seu limite de saque foi atingido.")  
        else:
            print(f"Você pode fazer {qtde_saques} saques.")
        print("==========================================")

    elif opcao_menu == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")