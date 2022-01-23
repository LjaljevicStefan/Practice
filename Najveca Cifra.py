n = int(input("Unesite vas broj: "))
najveca_cifra = 0
a = n
suma = 0
i = 0
while n != 0:
    cifra = n % 10
    n = n // 10
    suma += cifra
    i += 1
    if cifra > najveca_cifra:
        najveca_cifra = cifra

print(najveca_cifra)

if a % najveca_cifra == 0:
    print("deljiv")
else:
    print("nije deljiv")


print(suma / i)