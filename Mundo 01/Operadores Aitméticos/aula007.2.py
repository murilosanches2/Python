n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2                                                                             #\n (quebrar linha)
e = n1 ** n2                                                                              #end=" " (junta os prints)
print("Resultados da soma: {}, do produto: {}, da divisão: {:.3f},".format(s, m, d), end=" ")
                                                          #{:.3f} representa  '3' casas decimais
print("da divisão inteira: {} e da exponênciação: {}".format(di, e))
