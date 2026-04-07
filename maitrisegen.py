from logging import lastResort
from xml.dom.expatbuilder import parseFragment

print("LES NOMBRES PREMIERS")
premier = 0
nbre = int(input("entrer un nombr entier"))
for i in range(2,nbre):
    if nbre % i==0:
            premier=premier+1
if premier==0:
    print(f"le nombre:{nbre} est  premier")
else:
    print(f"le nombre{nbre}:n'est pas  premier")

print("NOMBRE PARFAIT")
parfait=int(input("entrer un entier"))
som=0
for i in range(1,parfait):
    if  parfait % i ==0:
        som=som+i
if som==parfait:
    print(f"le nombre {parfait} est un nombre parfait")
else:
    print(f"le nombre{parfait} n'est pas parfait")
print("LA DERNIERE LETTRE D4UN MOT")
mot=input("enter un mot ")
print(f"la dernierre lettere du mot entrer est ")
print(mot[-1])
print(len(mot))
print("INVERSER UN MOT")
LIB=[]
for i in range(len(mot)-1,-1,-1):
    LIB.append(mot[i])
print(LIB) 


