def afficher_menu():
    print("=== GESTIONNAIRE DE NOTES ===")
    print("1. Ajouter un étudiant")
    print("2. Afficher le bulletin")
    print("3. Voir le meilleur étudiant")
    print("4. Quitter")
def ajouter_etudiant(etudiants):
    nom = input("Nom de l'étudiant : ")
    notes = []
    nb = int(input("Combien de notes ? "))
    for i in range(nb):
        note = float(input(f"Note {i+1} : "))
        notes.append(note)
    etudiants.append({"nom": nom, "notes": notes})
    print(f"✅ {nom} ajouté avec succès !")


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