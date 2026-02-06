from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Medicine, Parent
from schemas import MedicineCreate, MedicineUpdate, MedicineResponse

router = APIRouter(tags=["Medicines"])


@router.get("/api/parents/{parent_id}/medicines", response_model=list[MedicineResponse])
def list_medicines(parent_id: int, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")
    return (
        db.query(Medicine)
        .filter(Medicine.parent_id == parent_id, Medicine.active == True)
        .all()
    )


@router.post("/api/parents/{parent_id}/medicines", response_model=MedicineResponse, status_code=201)
def add_medicine(parent_id: int, data: MedicineCreate, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")
    med = Medicine(parent_id=parent_id, **data.model_dump())
    db.add(med)
    db.commit()
    db.refresh(med)
    return med


@router.put("/api/medicines/{medicine_id}", response_model=MedicineResponse)
def update_medicine(medicine_id: int, data: MedicineUpdate, db: Session = Depends(get_db)):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(404, "Medicine not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(med, field, value)
    db.commit()
    db.refresh(med)
    return med


@router.delete("/api/medicines/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(404, "Medicine not found")
    med.active = False
    db.commit()
    return {"message": "Medicine deactivated"}
