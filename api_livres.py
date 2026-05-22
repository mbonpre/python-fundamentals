from fastapi import FastAPI
from pydantic import BaseModel
from functools import reduce
app=FastAPI()
#GET /livres → tous les livres
#GET /livres/{titre} → un livre par titre
#POST /ajoute_livres → ajouter un livre
#DELETE /livres/{titre} → supprimer un livre
#GET /stats → nombre total de livres + nombre total de pages
livres = [
    {"titre": "Python Crash Course", "auteur": "Eric Matthes", "pages": 544},
    {"titre": "Clean Code", "auteur": "Robert Martin", "pages": 431},
]
class NouveauLivres(BaseModel):
    titre :str
    auteur :str
    pages :int
@app.get("/livres")
def tousleslivres():
        return livres
@app.get("/livres/{titre}")
def obtenir_livre(titre:str):
    for e in livres:
        if e["titre"].lower()==titre.lower():
            return e
    return {"message":f"le livre est introuvable"}
@app.post("/ajoute_livres/")
def ajoute_livres(nouveau_livre:NouveauLivres):
    livres.append({"titre": nouveau_livre.titre, "auteur": nouveau_livre.auteur, "pages": nouveau_livre.pages})
    return {"message":f"livre{nouveau_livre.titre}"}
@app.delete("/supprimer_livres/{nom}")
def supprimer_livre(titre:str):
    for e in livres:
        if e["titre"].lower()==titre.lower():
            livres.remove(e)
            return{"message":f"le livre{titre} a ete suprimer avec succèes"}
    return {"message":f"le {titre} est introuvable"}
@app.get("/stats")
def getstate():
        total_pages = sum(e["pages"] for e in livres)
        return {"nombres de livres": len(livres), "total pages": total_pages}


