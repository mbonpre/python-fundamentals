import json
etudiants=[]
#sauvagarder
with open("etudiants.json","w") as f:
    json.dump(etudiants,f)
print("fichier sauvegarder !")
#Relire
def lire_fichier():
    try:
        with open("etudiants.json","r")  as f:
            data=json.load(f)
        print(data)
    except FileNotFoundError:
        print("fichier introuvable")
    except Exception as e:
        print(f"Erreur : {e}")
resultat=lire_fichier()
print(resultat)
