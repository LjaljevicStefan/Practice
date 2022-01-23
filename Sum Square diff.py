
n = int(input("Unesite broj: "))
i = 1
suma1 = 0
suma2 = 0

while i <= n:
    suma1 += i**2
    suma2 += i
    i += 1

suma2 = suma2**2

print(suma2 - suma1)