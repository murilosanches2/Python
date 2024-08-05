n1 = float(input("Insira a primeira nota do aluno: "))
n2 = float(input("Insira a segunda nota do aluno: "))
media = (n1 + n2) / 2
if media < 5:
    print("Média: {:.2f}\nREPROVADO!".format(media))
elif (media >= 5) and (media < 7):
    print("Média: {:.2f}\nRECUPERAÇÃO!".format(media))
else:
    print("Média: {:.2f}\nAPROVADO".format(media))
