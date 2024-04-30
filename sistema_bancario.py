
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_valor_saldo = valor > saldo

        excedeu_valor_limite = valor > limite

        excedeu_quantidade_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_valor_saldo:
            print("Falha na operação! Saldo insuficente")
        
        elif excedeu_valor_limite:
            print("Falha na operação! Valor do saque excede ao limite definido")

        elif excedeu_quantidade_saques:
            print("Falha na operação! Quantidade de saques excedida")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n===================== EXTRATO BANCÁRIO =====================\n")
        print("Conta sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {valor:.2f}")
        print("\n============================================================\n")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Falha na operação! Opção inválida.\nSelecione a opção desejada:")