soma = int(input("Digite o numero: "))

contador = 0

while soma != 0:
    contador += soma
    soma = int(input("Digite o próximo numero: "))
    if soma == 0:
        print("Ok")
        print(contador)
        break

