from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/businesses/", response_model=schemas.MedicalBusiness)
def create_business(business: schemas.MedicalBusinessCreate, db: Session = Depends(get_db)):
    return crud.create_medical_business(db=db, business=business)

@app.get("/businesses/", response_model=list[schemas.MedicalBusiness])
def read_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_medical_businesses(db=db, skip=skip, limit=limit)
