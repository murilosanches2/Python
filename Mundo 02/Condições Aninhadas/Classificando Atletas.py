pessoa = int(input("Insira o ano em que nasceu: "))
idade = 2024 - pessoa
if idade <= 9:
    print("Categoria: MIRIM")
elif (idade > 9) and (idade <= 14):
    print("Categoria: INFANTIL")
elif (idade > 14) and (idade <=19):
    print("Categoria: JUNIOR")
elif idade <= 20:
    print("Categoria: SENIOR")
elif idade > 20:
    print("Categoria: MASTER")
