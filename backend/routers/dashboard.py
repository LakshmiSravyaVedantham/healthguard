from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta
from database import get_db
from models import Parent, Medicine, HealthCheckin, MedicineLog, Alert
from schemas import DashboardResponse

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/{parent_id}", response_model=DashboardResponse)
def get_dashboard(parent_id: int, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")

    today = date.today()
    week_ago = today - timedelta(days=7)

    # Today's check-in
    todays_checkin = (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent_id, HealthCheckin.checkin_date == today)
        .first()
    )

    # 7-day check-ins
    checkins_7d = (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent_id, HealthCheckin.checkin_date >= week_ago)
        .order_by(HealthCheckin.checkin_date.desc())
        .all()
    )

    # Medicine adherence (7 days)
    logs_7d = (
        db.query(MedicineLog)
        .filter(MedicineLog.parent_id == parent_id, MedicineLog.scheduled_date >= week_ago)
        .all()
    )
    total_logs = len(logs_7d)
    taken_logs = sum(1 for l in logs_7d if l.taken)
    adherence = round((taken_logs / total_logs) * 100, 1) if total_logs > 0 else 0

    # Today's medicines
    todays_medicines = (
        db.query(Medicine)
        .filter(Medicine.parent_id == parent_id, Medicine.active == True)
        .all()
    )

    # Medicines taken today
    todays_med_logs = (
        db.query(MedicineLog)
        .filter(MedicineLog.parent_id == parent_id, MedicineLog.scheduled_date == today)
        .all()
    )
    medicines_taken = sum(1 for l in todays_med_logs if l.taken)

    # Recent alerts (last 10)
    recent_alerts = (
        db.query(Alert)
        .filter(Alert.parent_id == parent_id)
        .order_by(Alert.created_at.desc())
        .limit(10)
        .all()
    )

    return DashboardResponse(
        parent=parent,
        todays_checkin=todays_checkin,
        medicine_adherence_7d=adherence,
        recent_alerts=recent_alerts,
        checkins_7d=checkins_7d,
        todays_medicines=todays_medicines,
        medicines_taken_today=medicines_taken,
        medicines_total_today=len(todays_medicines),
    )
