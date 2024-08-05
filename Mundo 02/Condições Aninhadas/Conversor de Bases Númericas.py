entrada = int(input("Insira 1 para converter em binário\nInsira 2 para converter em octal\nInsira 3 para converter"
                    " em hexadecimal\nDigite o número: "))
if entrada == 1:
    print("Você escolheu binário!")
    numero = int(input("Digite um número inteiro: "))
    binario = bin(numero)
    print("O número em binário é: {}".format(binario[2:]))
elif entrada == 2:
    print("Você escolheu octal!")
    numero = int(input("Digite um número inteiro: "))
    octal = oct(numero)
    print("O número em binário é: {}".format(octal[2:]))
elif entrada == 3:
    print("Você escolheu hexadecimal!")
    numero = int(input("Digite um número inteiro: "))
    hexadecimal = hex(numero)
    print("O número em binário é: {}".format(hexadecimal[2:]))
else:
    print("Escolha inválida!")
