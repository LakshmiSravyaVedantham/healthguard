from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import jwt
import bcrypt
from database import get_db
from models import FamilyMember, Parent
from schemas import FamilyRegister, FamilyLogin, TokenResponse, FamilyResponse
from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRY_HOURS

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=FamilyResponse, status_code=201)
def register_family(data: FamilyRegister, db: Session = Depends(get_db)):
    # Verify parent exists
    parent = db.query(Parent).filter(Parent.id == data.parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")

    # Check duplicate email
    existing = db.query(FamilyMember).filter(FamilyMember.email == data.email).first()
    if existing:
        raise HTTPException(400, "Email already registered")

    password_hash = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()
    family = FamilyMember(
        name=data.name,
        email=data.email,
        password_hash=password_hash,
        phone=data.phone or "",
        parent_id=data.parent_id,
    )
    db.add(family)
    db.commit()
    db.refresh(family)
    return family


@router.post("/login", response_model=TokenResponse)
def login(data: FamilyLogin, db: Session = Depends(get_db)):
    family = db.query(FamilyMember).filter(FamilyMember.email == data.email).first()
    if not family:
        raise HTTPException(401, "Invalid email or password")

    if not bcrypt.checkpw(data.password.encode(), family.password_hash.encode()):
        raise HTTPException(401, "Invalid email or password")

    expire = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRY_HOURS)
    token_data = {
        "sub": str(family.id),
        "email": family.email,
        "parent_id": family.parent_id,
        "exp": expire,
    }
    token = jwt.encode(token_data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return TokenResponse(
        access_token=token,
        family_member=family,
    )
