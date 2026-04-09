#Partes do saldo
saldo = 1000

#senha
cartao_block = False
tentativa = input("Digite a senha : ")
quantidade_tentativas = 1
senha = "2701"
max_tentativas = 2
while tentativa != senha:
    tentativa = input("Digite a senha: ")
    quantidade_tentativas += 1
    if tentativa == senha:
        print("Senha correta!")
    elif tentativa == senha:
        print("senha correta!",pergunta_geral)
    elif quantidade_tentativas > max_tentativas:
        cartao_block = True
        print("Limite de tentativas excedido cartão congelado!")
        break
#perguntas

if cartao_block == True:
    pass
else:
    while cartao_block == False:
        pergunta_geral = input(
            """Digite 1 se você deseja saber seu saldo | 
            Digite 2 se você quer depositar saldo | 
            Digite 3 se você quer sacar dinheiro | 
            Digite 4 se você quer sair | Digite um desses números: 
            """)
        if pergunta_geral == "1":
            print("O seu saldo é de: EUR", saldo)
        elif pergunta_geral == "2":
            deposito = float(input("Digite a quantidade desejada para ser depositada: EUR"))
            saldo = deposito + saldo
            print(deposito)
        elif pergunta_geral == "3":
            sacar = float(input("Digite a quantidade desejada para ser sacada: EUR"))
            print(sacar)
            if sacar < saldo:
                saldo = saldo - sacar
                print("Saldo insuficiente")
        elif pergunta_geral == "4":
            print("Você saiu")
            break

