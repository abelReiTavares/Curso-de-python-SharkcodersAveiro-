quantidade_multas = float(input("Digite a quantidade de multas que você já teve no total:"))
velocidade = float(input("Digite a velocidade do carro:"))
valor_multa = (velocidade - 80) * 7.00
valor_multa2 = (velocidade - 80) * 20
valor_multa3 = (valor_multa2 * 2)

if   velocidade < 81:
    print("Boa viagem dirija com segurança!")
elif velocidade > 100:
    print("Você foi multado por multa grave EUR",valor_multa2)
if quantidade_multas > 3:
    print("Você foi multado muitas vezes o valor da multa dobrou EUR",valor_multa3)
else:
    print(f"Você foi multado {valor_multa} EUR")

