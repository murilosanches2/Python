n1 =int(input("Digite o primeiro valor: "))
n2 =int(input("Digite o segundo valor: "))
n3 =int(input("Digite o terceiro valor: "))

if n1 > n2:
    maior = n1
else:
    maior = n2
if maior > n3:
    maior = maior
    print("O maior número é: {}!".format(maior))
else:
    maior = n3
    print("O maior número é: {}!".format(maior))

if n1 < n2:
    menor = n1
else:
    menor = n2
if menor < n3:
    menor = menor
    print("O menor número é: {}!".format(menor))
else:
    menor = n3
    print("O menor número é: {}!".format(menor))
