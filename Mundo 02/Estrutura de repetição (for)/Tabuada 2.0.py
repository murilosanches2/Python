n = int(input("Digite um número: "))
print("\nTABUADA DO {}\n".format(n))
for c in range(1, 11):
    res = n * c
    print("{} X {} = {}".format(n,c,res))
print("\nFIM!")
