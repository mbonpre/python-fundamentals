from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

# Connexion à PostgreSQL
DATABASE_URL = "postgresql://postgres:katsuki1506@localhost/ecole"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Modèle de table
class EtudiantDB(Base):
    __tablename__ = "etudiants"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    age = Column(Integer)
    moyenne = Column(Float)

# Créer la table
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Modèle Pydantic
class EtudiantCreate(BaseModel):
    nom: str
    age: int
    moyenne: float

# Routes
@app.get("/etudiants")
def get_etudiants():
    with Session(engine) as session:
        etudiants = session.query(EtudiantDB).all()
        return etudiants

@app.post("/etudiants")
def creer_etudiant(etudiant: EtudiantCreate):
    with Session(engine) as session:
        db_etudiant = EtudiantDB(
            nom=etudiant.nom,
            age=etudiant.age,
            moyenne=etudiant.moyenne
        )
        session.add(db_etudiant)
        session.commit()
        session.refresh(db_etudiant)
        return db_etudiant
# GET un étudiant par ID
@app.get("/etudiants/{id}")
def get_etudiant(id: int):
    with Session(engine) as session:
        etudiant = session.get(EtudiantDB, id)
        if not etudiant:
            raise HTTPException(status_code=404, detail="Étudiant introuvable")
        return etudiant

# DELETE un étudiant par ID
@app.delete("/etudiants/{id}")
def supprimer_etudiant(id: int):
    with Session(engine) as session:
        etudiant = session.get(EtudiantDB, id)
        if not etudiant:
            raise HTTPException(status_code=404, detail="Étudiant introuvable")
        session.delete(etudiant)
        session.commit()
        return {"message": f"Étudiant {etudiant.nom} supprimé"}