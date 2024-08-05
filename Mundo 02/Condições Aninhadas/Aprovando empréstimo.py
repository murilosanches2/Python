v_casa = float(input("Insira o valor da casa, R$:"))
salario = float(input("Insira o valor do seu salário, R$:"))
tempo = int(input("Insira em quantos anos deseja quitar, R$:"))
prestação = v_casa / (tempo * 12)
limite_salario = salario * 0.3
if prestação > limite_salario:
    print("Infelizmente você não pode financiar essa casa, pois seu salário é de R${:.2f} e a prestação excedeu os 30%,"
          " R$:{:.2f}".format(salario,prestação))
else:
    print("Financiamento aprovado, você pagará um total de R${:.2f} por {} meses".format(prestação,(tempo*12)))