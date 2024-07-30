salario = float(input("Insira em reais o seu sálario, R$:"))
if salario > 1250.00:
    aumento = salario * 0.1
    print("Você terá um aumento de R$:{:.2f} reais!".format(aumento))
else:
    aumento = salario * 0.15
    print("Você terá um aumento de R$:{:.2f} reais!".format(aumento))
