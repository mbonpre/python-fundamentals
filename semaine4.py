import json
from functools import reduce

def afficher_menu():
    print("=== GESTIONNAIRE DE NOTES ===")
    print("1. Ajouter un étudiant")
    print("2. Afficher le bulletin")
    print("3. Voir le meilleur étudiant")
    print("4. Moyenne générale")
    print("5. Afficher les admis")
    print("6. Classement")
    print("7. Quitter")

def ajouter_etudiant(etudiants):
    nom = input("Nom de l'étudiant : ")
    notes = []
    n = int(input("Combien de notes ? "))
    for i in range(n):
        while True:
            try:
                note = float(input(f"Note {i+1} : "))
                if 0 <= note <= 20:
                    notes.append(note)
                    break
                else:
                    print(" Note invalide (entre 0 et 20)")
            except ValueError:
                print(" Entre un nombre valide")
    etudiants.append({"nom": nom, "notes": notes})
    with open("etudiants.json", "w") as f:
        json.dump(etudiants, f, indent=4)
    print(f"{nom} ajouté et sauvegardé !")

def afficher_bulletin(etudiants):
    if not etudiants:
        print(" Aucun étudiant enregistré !")
        return
    resultat = list(map(lambda e: {
        "nom": e["nom"],
        "moyenne": round(sum(e["notes"])/len(e["notes"]), 2)
    }, etudiants))
    bulletin = sorted(resultat, key=lambda e: e["moyenne"], reverse=True)
    print("\n=== BULLETIN ===")
    for e in bulletin:
        print(f" {e['nom']} | Moyenne : {e['moyenne']}")
    print("================\n")

def meilleur_etudiant(etudiants):
    if not etudiants:
        print(" Aucun étudiant enregistré !")
        return
    meilleur = max(etudiants, key=lambda e: sum(e["notes"])/len(e["notes"]))
    moy = round(sum(meilleur["notes"])/len(meilleur["notes"]), 2)
    print(f"\n🏆 Meilleur étudiant : {meilleur['nom']} avec {moy}/20\n")

def moyenne_generale(etudiants):
    moyennes = list(map(lambda e: sum(e["notes"])/len(e["notes"]), etudiants))
    return round(reduce(lambda a, b: a + b, moyennes) / len(moyennes), 2)

def afficher_admis(etudiants):
    admis = list(filter(lambda e: sum(e["notes"])/len(e["notes"]) >= 10, etudiants))
    if not admis:
        print(" Aucun étudiant admis !")
        return
    print("\n=== ADMIS ===")
    for e in admis:
        moy = round(sum(e["notes"])/len(e["notes"]), 2)
        print(f"✅ {e['nom']} — {moy}/20")
    print("=============\n")

def classement(etudiants):
    trie = sorted(etudiants, key=lambda e: sum(e["notes"])/len(e["notes"]), reverse=True)
    print("\n=== CLASSEMENT ===")
    for i, e in enumerate(trie):
        moy = round(sum(e["notes"])/len(e["notes"]), 2)
        print(f"{i+1}. {e['nom']} — {moy}/20")
    print("==================\n")

def main():
    try:
        with open("etudiants.json", "r") as f:
            etudiants = json.load(f)
    except FileNotFoundError:
        etudiants = []

    while True:
        afficher_menu()
        choix = input("Ton choix : ")

        if choix == "7":
            print("Au revoir !")
            break
        elif choix == "1":
            ajouter_etudiant(etudiants)
        elif choix == "2":
            afficher_bulletin(etudiants)
        elif choix == "3":
            meilleur_etudiant(etudiants)
        elif choix == "4":
            if not etudiants:
                print(" Aucun étudiant enregistré !")
            else:
                print(f"\n📊 Moyenne générale : {moyenne_generale(etudiants)}/20\n")
        elif choix == "5":
            afficher_admis(etudiants)
        elif choix == "6":
            classement(etudiants)
        else:
            print(" Choix invalide !")

main()