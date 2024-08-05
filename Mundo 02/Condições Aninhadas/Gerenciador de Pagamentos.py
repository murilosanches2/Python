import os
produto = float(input("Insira o valor do produto: R$"))
escolher = int(input('''Insira a forma de pagamento:
[1] -> À vista! (10% de desconto)
[2] -> À vista no CARTÃO! (5% de desconto)
[3] -> Até 2x no cartão, sem juros!
[4] -> Até 3x ou mais no cartão! (20% de juros)\n'''))

if escolher == 1:
    preco = produto - (produto * 0.1)
    print("Com 10% de desconto à vista o preço fica R${:.2f}. Obrigado!!".format(preco))
elif escolher == 2:
    preco = produto - (produto * 0.05)
    print("Com 5% de desconto à vista no cartão, o preço fica R${:.2f}. Obrigado!!".format(preco))
elif escolher == 3:
    preco = produto / 2
    print("2x no cartão! O preço de cada parcela é R${:.2f}. Obrigado!!".format(preco))
elif escolher == 4:
    vezes = int(input("Insira o número de vezes que deseja parcelar: "))
    preco = (produto + (produto * 0.2)) / vezes
    print("{}x cartão! O preço de cada parcela é de R${:.2f}, com 20% de juros. Obrigado!!".format(vezes, preco))