#casting (trocar o tipo de dados)
#1 / Divisão
#3 + soma
#3 - subtração
#2 * multiplicação
#2 // Divisão inteira
#1 ** Potência

#Item 1
Dados1 = input("Digite o nome do produto 1: ")
Preço1 = float(input("Digite o preço do produto 1 em euros: "))
Quantidade1 = float(input("Digite a quantidade desejada do produto 1: "))

print ("Nome do produto 1:",Dados1,", preço do produto 1, €",Preço1,"e a quantidade de produtos",Quantidade1,",","Preço total do produto 1, €",Preço1,)

Dados2 = input("Digite o nome do produto 2: ")
Preço2 = float(input("Digite o preço do produto 2 em euros: "))
Quantidade2 = float(input("Digite a quantidade desejada do produto 2: "))

print ("Nome do produto 2:",Dados2,", preço do produto 2, €",Preço2,"e a quantidade de produtos",Quantidade2,",","Preço total do produto 2, €",Preço2,)

Dados3 = input("Digite o nome do produto 3: ")
Preço3 = float(input("Digite o preço do produto 3 em euros: "))
Quantidade3 = float(input("Digite a quantidade desejada do produto 3: "))

print ("Nome do produto 3:",Dados3,", preço do produto 3, €",Preço3,"e a quantidade de produtos",Quantidade3,",","Preço total do produto 3, €",Preço3,)

preço_total1 = Preço1 * Quantidade1

preço_total2 = Preço2 * Quantidade2

preço_total3 = Preço3 * Quantidade3

preço_total = Preço1 * Quantidade1 + Preço2 * Quantidade2 + Preço3 * Quantidade3

print("Preço total de todos produtos €",preço_total,)

decisao = input("Você deseja comprar?")
if decisao == "Sim":
    print("Produtos enviados")
else:
    print("Produtos deletados")
print("Preço total de todos produtos €",preço_total,)



