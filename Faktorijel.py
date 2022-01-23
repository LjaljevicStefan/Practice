#n = int(input("Unesite vas broj: "))

def fakt(broj):
    if broj == 0:
        return 1
    elif broj < 0:
        return "ne moze"
    else:
        return broj * fakt(broj - 1)

while 1:
    n = int(input("Unesite vas broj: "))
    print(fakt(n))
    if n < 0:
        break
