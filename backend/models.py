from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    language = Column(String(10), default="telugu")  # telugu, english, both
    age = Column(Integer)
    health_conditions = Column(Text, default="")
    emergency_contact_phone = Column(String(20), default="")
    active = Column(Boolean, default=True)
    conversation_state = Column(String(50), default="new")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    family_members = relationship("FamilyMember", back_populates="parent")
    medicines = relationship("Medicine", back_populates="parent")
    checkins = relationship("HealthCheckin", back_populates="parent")
    medicine_logs = relationship("MedicineLog", back_populates="parent")
    alerts = relationship("Alert", back_populates="parent")


class FamilyMember(Base):
    __tablename__ = "family_members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False, index=True)
    password_hash = Column(String(200), nullable=False)
    phone = Column(String(20), default="")
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent = relationship("Parent", back_populates="family_members")


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
    name = Column(String(100), nullable=False)
    name_telugu = Column(String(200), default="")
    dosage = Column(String(100), default="")
    time_slot = Column(String(20), nullable=False)  # morning, afternoon, night
    time_exact = Column(String(10), default="")  # e.g. "08:00"
    instructions = Column(Text, default="")
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent = relationship("Parent", back_populates="medicines")
    logs = relationship("MedicineLog", back_populates="medicine")


class HealthCheckin(Base):
    __tablename__ = "health_checkins"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
    checkin_date = Column(Date, nullable=False)
    feeling = Column(Integer, default=2)  # 1=good, 2=ok, 3=bad
    bp_systolic = Column(Integer)
    bp_diastolic = Column(Integer)
    sugar_level = Column(Float)
    pain_level = Column(Integer)  # 1-5
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent = relationship("Parent", back_populates="checkins")


class MedicineLog(Base):
    __tablename__ = "medicine_logs"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    scheduled_date = Column(Date, nullable=False)
    time_slot = Column(String(20), nullable=False)
    taken = Column(Boolean, default=False)
    confirmed_at = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent = relationship("Parent", back_populates="medicine_logs")
    medicine = relationship("Medicine", back_populates="logs")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
    family_member_id = Column(Integer, ForeignKey("family_members.id"), nullable=True)
    alert_type = Column(String(50), nullable=False)  # health_bad, medicine_missed, sos, inactivity
    message = Column(Text, nullable=False)
    resolved = Column(Boolean, default=False)
    resolved_at = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    parent = relationship("Parent", back_populates="alerts")
    family_member = relationship("FamilyMember")
