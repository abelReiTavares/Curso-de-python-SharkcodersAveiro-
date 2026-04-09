tentativa = input("Digite a senha : ")
quantidade_tentativas = 1
senha = "senha_doProfessor"
max_tentativas = 2
while tentativa != senha:
    tentativa = input("Digite a senha: ")
    quantidade_tentativas += 1
    if tentativa == senha:
        print("Senha correta!")
    elif tentativa == senha:
        print("senha correta!")
    elif quantidade_tentativas > max_tentativas:
        print("Limite de tentativas excedido")
        break