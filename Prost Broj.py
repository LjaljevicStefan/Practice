n = int(input("Unesite vas broj: "))
i = 2
prost = True

if n == 1:
    prost = False

while i < n:
    if n % i == 0:
        prost = False
    i += 1

print(prost)