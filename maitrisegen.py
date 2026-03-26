print("calcule la moyenne des elements entrer jus qu'a un chiffre negatif")
print("enter les nombres voulu ")
som=0
b=0
while b==0:
    i=int(input( ))
    if i>=0:
        som=som+i
    else:
        b=1
print(f"la somme des nombre entrer est {som}")
