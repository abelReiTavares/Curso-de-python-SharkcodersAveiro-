numero1 = int(input("Digite o primeiro  de ínicio desejado: "))
numero2 = int(input("Digite o segundo número desejado (fim): "))

contador = 0
for numero in range(numero1, numero2+1):
    contador += numero


print(contador)




