import numpy as np

A = [[21, 23, 19, 18, 19, 17, 16],
     [20, 22, 21, 19, 16, 18, 18],
     [20, 21, 19, 17, 17, 16, 17],
     [21, 22, 19, 18, 19, 16, 17],
     [24, 23, 19, 20, 20, 19, 20],
     [21, 18, 19, 20, 20, 20, 18],
     [19, 19, 18, 17, 20, 21, 20],
     [20, 20, 19, 17, 16, 16, 17],
     [16, 15, 17, 19, 15, 16, 20],
     [20, 17, 18, 20, 24, 25, 24]]

prosecne_T = []
najhladnije = []
najtoplije = []
dani = ["pon", "uto", "sre", "cet", "pet", "sub", "ned"]
gradovi = ["Beograd", "Nis", "Novi Sad", "Obr", "Kraljevo", "Kragujevac", "Pancevo", "Krusevac", "Vranje", "Leskovac"]
a = 0

for i in A:
    prosecna_T = 0
    grad = gradovi[a]
    for j in i:
        prosecna_T += j
    if prosecna_T / 7 - prosecna_T // 7 > 0.5:
        prosecne_T.append(grad)
        prosecne_T.append(prosecna_T // 7 + 1)
    else:
        prosecne_T.append(grad)
        prosecne_T.append(prosecna_T // 7)
    a += 1

for i in np.transpose(A):
    a = i[0]
    for j in i:
        if j < a:
            a = j
        else:
            a = a
    najhladnije.append(a)

for i in A:
    a = i[0]
    for j in i:
        if j > a:
            a = j
        else:
            a = a
    najtoplije.append(a)

print(prosecne_T)
print(najhladnije)
print(najtoplije)