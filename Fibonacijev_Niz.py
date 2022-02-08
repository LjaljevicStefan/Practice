# Fibonacijev Niz

n = int(input("Unesite duzinu niza: "))
niz = [0, 1]
i = 1

while i <= n:
    x = niz[-1] + niz[-2]
    niz.append(x)
    i += 1

print(niz)
