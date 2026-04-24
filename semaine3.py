import json
def afficher_menu():
    print("=== GESTIONNAIRE DE NOTES ===")
    print("1. Ajouter un étudiant")
    print("2. Afficher le bulletin")
    print("3. Voir le meilleur étudiant")
    print("4. Quitter")


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
                    break  # ✅ on sort de la boucle si c'est valide
                else:
                    print("❌ Note invalide (entre 0 et 20)")

            except ValueError:
                print("❌ Entre un nombre valide")1

    etudiants.append({"nom": nom, "notes": notes})

    with open("etudiants.json", "w") as f:
        json.dump(etudiants, f, indent=4)

    print(f"✅ {nom} ajouté et sauvegardé !")


def afficher_bulletin(etudiants):
    if not etudiants:
        print("❌ Aucun étudiant enregistré !")
        return

    resultat = []
    for e in etudiants:
        moy = sum(e["notes"]) / len(e["notes"])
        resultat.append({"nom": e["nom"], "moyenne": round(moy, 2)})

    bulletin = sorted(resultat, key=lambda e: e["moyenne"], reverse=True)

    print("\n=== BULLETIN ===")
    for e in bulletin:
        print(f"👤 {e['nom']} | Moyenne : {e['moyenne']}")
    print("================\n")


def meilleur_etudiant(etudiants):
    if not etudiants:
        print("❌ Aucun étudiant enregistré !")
        return

    meilleur = max(etudiants, key=lambda e: sum(e["notes"]) / len(e["notes"]))
    moy = sum(meilleur["notes"]) / len(meilleur["notes"])
    print(f"\n🏆 Meilleur étudiant : {meilleur['nom']} avec {round(moy, 2)}/20\n")
def main():
    etudiants = []
    try:
        with open("etudiants.json", "r") as f:
            etudiants = json.load(f)
    except FileNotFoundError:
        etudiants = []
    while True:
        afficher_menu()
        choix = input("Ton choix : ")

        if choix == "4":
            print("Au revoir !")
            break
        elif choix == "1":
            ajouter_etudiant(etudiants)
        elif choix == "2":
            afficher_bulletin(etudiants)
        elif choix == "3":
            meilleur_etudiant(etudiants)

main()