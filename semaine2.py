class etu:
    def __init__(self,nom,age,note=None):
        self.nom=nom
        self.age = age
        self.note = note if note is not None else []

    def se_presenter(self):
       print(f"je me nomme {self.nom} et j'ai {self.age} ")
    def calculerMoyenne(self):
        moy=sum(self.note)/len(self.note)
        return moy
    def mention(self):
        moy = self.calculerMoyenne()

        if moy < 10:
           return f"Insuffisant"
        elif 10 <= moy <= 12:
           return f"assable"
        elif 12 < moy <= 14:
          return  f"Assez bien"
        elif 14 < moy <= 16:
         return   f"Bien"
        else:
           return f"Très bien"
    def ajouternote(self,p):
        self.note.append(p)
class Promotion:
    def __init__(self):
        self.etudiants=[]
    def ajouter_etudiants(self,etudiant):
        self.etudiants.append(etudiant)
    def meilleuretudiant(self):
        meilleur= max(self.etudiants,key=lambda e:e.calculerMoyenne())
        print(f"le meilleur etudiant est {meilleur.nom}")
    def affichage_classement(self):
        etudiants_tri=sorted(self.etudiants,key=lambda e:e.calculerMoyenne(),reverse=True)
        #print(etudiants)
        print("le classemnt des meilleurs etudiants")
        for i in etudiants_tri:
            print(f"je m'appelle {i.nom} et j'ai {i.age}:j'ai {i.calculerMoyenne()} de moyenne  avec {i.mention()} comme mention")
class professeur:
    def __init__(self,nom,matiere):
        self.nom=nom
        self.matiere=matiere
    def note (self,etudiant,note):
          etudiant.note.append(note)
    def afficher_classe(self,x):
        x.affichage_classement()


#crer un objet
etudiant=etu("Jennifer",18,[20,15])
etudiant.se_presenter()
print(f" la moyenne est {etudiant.calculerMoyenne()}")
etudiant.ajouternote(0)
#print(f"la nouvelle mention est{etudiant.calculerMoyenne()}")
print(f"la mention est {etudiant.mention()}")
promo=Promotion()
e1=etu("Précieux" ,19,[11,20])
e2=etu("romain" ,19,[9,0,10])
e3=etu("otavio" ,19,[12,20,11])
promo.ajouter_etudiants(e1)
promo.ajouter_etudiants(e2)
promo.ajouter_etudiants(e3)
o=promo.meilleuretudiant()
print(f"le meilleur etudiant est {o}")
promo.affichage_classement()
prof=professeur("NAMBONI","informatique")
prof.note(e1,20)
prof.afficher_classe(promo)

