def rast(broj_stabala, procenat, godine):
    x = 1
    while x <= godine:
        broj_stabala *= 1 + 0.01 * procenat
        x += 1
    return broj_stabala


rezultat = rast(1000, 20, 200)
print(rezultat)
