# S = 1/2 - 1/3 + 1/4 - 1/5 + ... + 1 / (i + 1)
from math import *

n = int(input("Unesite vas broj: "))
i = 1
S = 1


while i <= n:
    S *= 1 / (i + 1)
    i += 1


print(S)
srednja_vrednost = S / n
print(srednja_vrednost)