niz = []


while 1:
    n = (input("Unesite vase brojeve: "))
    niz.append(n)
    if n == "":
        del(niz[-1])
        break

print(niz)