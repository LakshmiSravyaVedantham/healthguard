from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


# --- Parent ---
class ParentCreate(BaseModel):
    name: str
    phone: str
    language: str = "telugu"
    age: Optional[int] = None
    health_conditions: Optional[str] = ""
    emergency_contact_phone: Optional[str] = ""

class ParentUpdate(BaseModel):
    name: Optional[str] = None
    language: Optional[str] = None
    age: Optional[int] = None
    health_conditions: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    active: Optional[bool] = None

class ParentResponse(BaseModel):
    id: int
    name: str
    phone: str
    language: str
    age: Optional[int]
    health_conditions: Optional[str]
    emergency_contact_phone: Optional[str]
    active: bool
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


# --- Family Member ---
class FamilyRegister(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = ""
    parent_id: int

class FamilyLogin(BaseModel):
    email: str
    password: str

class FamilyResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    parent_id: int

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    family_member: FamilyResponse


# --- Medicine ---
class MedicineCreate(BaseModel):
    name: str
    name_telugu: Optional[str] = ""
    dosage: Optional[str] = ""
    time_slot: str  # morning, afternoon, night
    time_exact: Optional[str] = ""
    instructions: Optional[str] = ""

class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    name_telugu: Optional[str] = None
    dosage: Optional[str] = None
    time_slot: Optional[str] = None
    time_exact: Optional[str] = None
    instructions: Optional[str] = None
    active: Optional[bool] = None

class MedicineResponse(BaseModel):
    id: int
    parent_id: int
    name: str
    name_telugu: Optional[str]
    dosage: Optional[str]
    time_slot: str
    time_exact: Optional[str]
    instructions: Optional[str]
    active: bool

    class Config:
        from_attributes = True


# --- Health Check-in ---
class CheckinCreate(BaseModel):
    checkin_date: date
    feeling: int  # 1=good, 2=ok, 3=bad
    bp_systolic: Optional[int] = None
    bp_diastolic: Optional[int] = None
    sugar_level: Optional[float] = None
    pain_level: Optional[int] = None
    notes: Optional[str] = ""

class CheckinResponse(BaseModel):
    id: int
    parent_id: int
    checkin_date: date
    feeling: int
    bp_systolic: Optional[int]
    bp_diastolic: Optional[int]
    sugar_level: Optional[float]
    pain_level: Optional[int]
    notes: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


# --- Medicine Log ---
class MedicineLogResponse(BaseModel):
    id: int
    parent_id: int
    medicine_id: int
    scheduled_date: date
    time_slot: str
    taken: bool
    confirmed_at: Optional[datetime]

    class Config:
        from_attributes = True


# --- Alert ---
class AlertResponse(BaseModel):
    id: int
    parent_id: int
    family_member_id: Optional[int]
    alert_type: str
    message: str
    resolved: bool
    resolved_at: Optional[datetime]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


# --- Dashboard ---
class DashboardResponse(BaseModel):
    parent: ParentResponse
    todays_checkin: Optional[CheckinResponse]
    medicine_adherence_7d: float
    recent_alerts: list[AlertResponse]
    checkins_7d: list[CheckinResponse]
    todays_medicines: list[MedicineResponse]
    medicines_taken_today: int
    medicines_total_today: int
