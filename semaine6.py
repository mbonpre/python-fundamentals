from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

etudiants = [
    {"nom": "Precieux", "notes": [15, 18, 12]},
    {"nom": "Amina", "notes": [18, 19, 17]},
    {"nom": "Koffi", "notes": [8, 10, 9]},
]

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur mon API !"}

@app.get("/etudiants")
def get_etudiants():
    return etudiants
@app.get("/etudiants/admis")
def get_admis():
        return list(filter(lambda x:sum(x["notes"])/len(x["notes"])>=10,etudiants))

@app.get("/meilleur-etudiant")
def get_meilleur():
    meilleur=max(etudiants,key=lambda e:sum(e["notes"]) / len(e["notes"]) )
    return meilleur

@app.get("/etudiants/{nom}")
def get_etudiant(nom: str):
    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            return e
    return {"erreur": "Étudiant introuvable"}

@app.get("/etudiants/{nom}/moyenne")
def get_moyenne(nom: str):
    for e in etudiants:                                
        if e["nom"].lower() == nom.lower():
            moy = sum(e["notes"]) / len(e["notes"])
            return {"nom": e["nom"], "moyenne": round(moy, 2)}
    return {"erreur": "Étudiant introuvable"}

# Modèle — structure attendue
class Etudiant(BaseModel):
    nom: str
    notes: list[float]
class NouvellesNotes(BaseModel):
    nouvellesnotes:list[float]

# Route POST
@app.post("/etudiants")
def creer_etudiant(etudiant: Etudiant):
    etudiants.append({"nom": etudiant.nom, "notes": etudiant.notes})
    return {"message": f"{etudiant.nom} ajouté avec succès !"}

@app.get("/stats")
def get_stats():
    return {"totale": len(etudiants), "admis":len(get_admis()), "recales":len(etudiants)-len(get_admis())}
@app.delete("/supp_etudiants/{nom}")
def supprimer_etudiants(nom:str):
    for e in etudiants:
        if nom.lower()==e["nom"].lower():
            etudiants.remove(e)
            return {"message": f"etudiants {nom} supprimer avec succèes"}
    return {"message":f"Etudiant{nom} introuvable!"}
@app.put("/ajouter_notes/{nom}")
def modifier_notes(nom: str, nouvelles_notes: NouvellesNotes):
    for e in etudiants:
        if nom.lower() == e["nom"].lower():
            e["notes"]=nouvelles_notes.nouvellesnotes
            return {"message":f" Etudiant {e["nom"]} modifier avec succès"}
    return {"message":f"Etudiant introuvable"}
