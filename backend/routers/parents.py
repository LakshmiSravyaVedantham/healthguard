from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Parent
from schemas import ParentCreate, ParentUpdate, ParentResponse

router = APIRouter(prefix="/api/parents", tags=["Parents"])


@router.get("", response_model=list[ParentResponse])
def list_parents(db: Session = Depends(get_db)):
    return db.query(Parent).filter(Parent.active == True).all()


@router.post("", response_model=ParentResponse, status_code=201)
def create_parent(data: ParentCreate, db: Session = Depends(get_db)):
    existing = db.query(Parent).filter(Parent.phone == data.phone).first()
    if existing:
        raise HTTPException(400, "Phone number already registered")
    parent = Parent(**data.model_dump())
    parent.conversation_state = "main_menu"
    db.add(parent)
    db.commit()
    db.refresh(parent)
    return parent


@router.get("/{parent_id}", response_model=ParentResponse)
def get_parent(parent_id: int, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")
    return parent


@router.put("/{parent_id}", response_model=ParentResponse)
def update_parent(parent_id: int, data: ParentUpdate, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(parent, field, value)
    db.commit()
    db.refresh(parent)
    return parent
