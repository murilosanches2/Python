n1 = int(input("Digite em cm, o valor da primeira reta: "))
n2 = int(input("Digite em cm, o valor da segunda reta: "))
n3 = int(input("Digite em cm, o valor da terceira reta: "))
if n1 == n2 == n3: #(n1+n2 > n3) and (n1+n3 > n2) and (n2+n3 > n1):
    print("Triângulo Equilátero!")
elif (n1 == n2) or (n1 == n3) or (n2 == n3):
    print("Triângulo Isósceles!")
elif n1 != n2 != n3:
    print("Triângulo Escaleno!")

