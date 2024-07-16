dia = int(input("Insira o total de dias com o carro: "))
km = float(input("Insira o total de KM's rodados com o carro: "))
cdia = dia * 60
ckm = km * 0.15
pagar = cdia + ckm
print("O custo final do aluguel ficou em: R${:.3f}!".format(pagar))
