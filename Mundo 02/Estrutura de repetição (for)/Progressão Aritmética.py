n = int(input("Primeiro termo:"))
r = int(input("Razão:"))
décimo: int = n + (10 - 1) * r
for c in range(n,décimo + r, r):
    print("{} ".format(c),end="-> ")
print("ACABOU")
