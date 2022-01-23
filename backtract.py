from random import randint
from numpy import matrix

dim = 50
A = matrix([[randint(0, 100) for i in range(dim)] for j in range(dim)])
print(A)

min_cena = A.sum()                                           
print('\nTotal sum (max sum): ' + str(min_cena))
put = ''
min_put = ''
svaki_put = ''
# funkcija koja pronalazi min put od bilo koje tacke (x,y) do cilja

def vozi(x,y,cena,put):                      # sa sobom uvek nosim dosadanju nakupljenu cenu i predjeni put
    global min_cena, min_put, svaki_put  
    cena += A[x,y]               # kako na koju tacku stanemo, dodamo tu tacku na koju smo stali u cenu
    put  += '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') '  # i u putanju
    korak = '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') '
    
    if x == dim-1 and y == dim-1:                              # ako smo stigli na cilj:
        if cena < min_cena:								   # proverimo da li je cena koju smo postigli manja od min_cena
            min_cena = cena                                # ako jeste, zamenimo min_cena sa novom postignutom minimalnom cenom 
            min_put = put
            svaki_put = ''                                 # i zamenimo min_put sa tim putem koji je za sada najbolji
    elif cena < min_cena and korak not in svaki_put:                                  # ako nismo stigli na cilj:
        if x < dim-1 :									   # ako moze desno
            vozi(x+1,y,cena,put)
            svaki_put += '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') '                           # vozi desno 
        if y < dim-1:                                      # ako moze dole
            vozi(x,y+1,cena,put)
            svaki_put += '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') ' 						   # vozi dole
        if x > 0:										   # ako moze levo
        	vozi(x-1,y,cena,put)
        	svaki_put += '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') '						   # vozi levo
        if y > 0:										   # ako moze gore
        	vozi(x,y-1,cena,put)
        	svaki_put += '-> ' + str(A[x,y]) + ' (' + str(x) + ',' + str(y) + ') '						   # vozi gore
        	                           # vozi dole 

# fora je da se svaki put kada stanemo na neku tacku x,y ponasamo kao da smo na pocetku novog zadatka da nadjemo najbolji put od te tacke x,y do cilja
# a za to imamo funkciju vozi. Samo je pozovemo od pocetne tacke 0,0 i stavimo pocetnu cenu 0 i pocetni prazan pocetni put 
# i pustimo je da vozi svuda gde moze dok ne dodje do cilja
vozi(0,0,0,put)
print('Najjeftinija cena puta: \t' + str(min_cena))
print('Najjeftiniji put: \t\t\t' + min_put)