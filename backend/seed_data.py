"""Seed demo data for Aarogya Saathi."""

import sys
from datetime import date, datetime, timedelta, timezone
import bcrypt
from database import SessionLocal, engine, Base
from models import Parent, FamilyMember, Medicine, HealthCheckin, MedicineLog, Alert


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Check if already seeded
    if db.query(Parent).first():
        print("Database already has data. Skipping seed.")
        db.close()
        return

    print("Seeding demo data...")

    # --- Parent ---
    parent = Parent(
        name="Lakshmi",
        phone="+919876543210",
        language="both",
        age=62,
        health_conditions="BP, Diabetes",
        emergency_contact_phone="+919876543211",
        conversation_state="main_menu",
    )
    db.add(parent)
    db.flush()

    # --- Family Member ---
    pw_hash = bcrypt.hashpw("demo123".encode(), bcrypt.gensalt()).decode()
    family = FamilyMember(
        name="Sravya",
        email="sravya@demo.com",
        password_hash=pw_hash,
        phone="+919876543211",
        parent_id=parent.id,
    )
    db.add(family)

    # --- Medicines ---
    medicines = [
        Medicine(parent_id=parent.id, name="Amlodipine", name_telugu="అమ్లోడిపిన్",
                 dosage="5mg", time_slot="morning", time_exact="08:00",
                 instructions="After breakfast"),
        Medicine(parent_id=parent.id, name="Metformin", name_telugu="మెట్‌ఫార్మిన్",
                 dosage="500mg", time_slot="morning", time_exact="08:00",
                 instructions="After breakfast"),
        Medicine(parent_id=parent.id, name="Metformin", name_telugu="మెట్‌ఫార్మిన్",
                 dosage="500mg", time_slot="night", time_exact="21:00",
                 instructions="After dinner"),
        Medicine(parent_id=parent.id, name="Calcium + D3", name_telugu="క్యాల్సియం",
                 dosage="1 tablet", time_slot="afternoon", time_exact="13:00",
                 instructions="After lunch"),
    ]
    db.add_all(medicines)
    db.flush()

    # --- Check-ins (past 14 days) ---
    import random
    today = date.today()
    feelings = [1, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 2, 1, 1]
    notes_map = {3: "Joint pain"}

    for i, feeling in enumerate(feelings):
        d = today - timedelta(days=13 - i)
        checkin = HealthCheckin(
            parent_id=parent.id,
            checkin_date=d,
            feeling=feeling,
            bp_systolic=random.randint(120, 145) if random.random() > 0.3 else None,
            bp_diastolic=random.randint(75, 92) if random.random() > 0.3 else None,
            sugar_level=random.randint(90, 160) if random.random() > 0.5 else None,
            notes=notes_map.get(feeling, ""),
        )
        db.add(checkin)

    # --- Medicine Logs (past 7 days) ---
    for i in range(7):
        d = today - timedelta(days=6 - i)
        for med in medicines:
            taken = random.random() > 0.15  # ~85% adherence
            log = MedicineLog(
                parent_id=parent.id,
                medicine_id=med.id,
                scheduled_date=d,
                time_slot=med.time_slot,
                taken=taken,
                confirmed_at=datetime.now(timezone.utc) if taken else None,
            )
            db.add(log)

    # --- Alerts ---
    alerts = [
        Alert(parent_id=parent.id, alert_type="health_bad",
              message="Lakshmi reported feeling bad: Joint pain",
              resolved=True,
              resolved_at=datetime.now(timezone.utc) - timedelta(days=5)),
        Alert(parent_id=parent.id, alert_type="medicine_missed",
              message="Lakshmi missed some medicines on " + str(today - timedelta(days=2)),
              resolved=False),
    ]
    db.add_all(alerts)

    db.commit()
    db.refresh(parent)
    parent_id = parent.id
    med_count = len(medicines)
    db.close()
    print("Demo data seeded successfully!")
    print(f"  Parent: Lakshmi (ID: {parent_id}, Phone: +919876543210)")
    print(f"  Family: Sravya (email: sravya@demo.com, password: demo123)")
    print(f"  Medicines: {med_count} added")
    print(f"  Check-ins: 14 days of history")
    print(f"  Medicine logs: 7 days of history")


if __name__ == "__main__":
    seed()
