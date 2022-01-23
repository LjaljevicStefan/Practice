X_koordinata = float(input("Unesite x koordinatu:"))
Y_koordinata = float(input("Unesite y koordinatu:"))

if X_koordinata > 0 and Y_koordinata > 0:
    print("I KVADRANT")
elif X_koordinata < 0 and Y_koordinata > 0:
    print("II KVADRANT")
elif X_koordinata < 0 and Y_koordinata < 0:
    print("III KVADRANT")
elif X_koordinata > 0 and Y_koordinata < 0:
    print("IV KVADRANT")
else:
    print("NE SMARAJ")