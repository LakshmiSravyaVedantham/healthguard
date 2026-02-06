from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta
from database import get_db
from models import HealthCheckin, MedicineLog, Parent
from schemas import CheckinResponse, MedicineLogResponse

router = APIRouter(tags=["Check-ins"])


@router.get("/api/parents/{parent_id}/checkins", response_model=list[CheckinResponse])
def list_checkins(
    parent_id: int,
    days: int = Query(30, ge=1, le=365),
    db: Session = Depends(get_db),
):
    _assert_parent(parent_id, db)
    since = date.today() - timedelta(days=days)
    return (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent_id, HealthCheckin.checkin_date >= since)
        .order_by(HealthCheckin.checkin_date.desc())
        .all()
    )


@router.get("/api/parents/{parent_id}/checkins/summary")
def checkin_summary(
    parent_id: int,
    days: int = Query(7, ge=1, le=365),
    db: Session = Depends(get_db),
):
    _assert_parent(parent_id, db)
    since = date.today() - timedelta(days=days)
    checkins = (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent_id, HealthCheckin.checkin_date >= since)
        .all()
    )
    total = len(checkins)
    if total == 0:
        return {"days": days, "total_checkins": 0, "avg_feeling": None, "good_days": 0, "ok_days": 0, "bad_days": 0}

    good = sum(1 for c in checkins if c.feeling == 1)
    ok = sum(1 for c in checkins if c.feeling == 2)
    bad = sum(1 for c in checkins if c.feeling == 3)
    avg = sum(c.feeling for c in checkins) / total

    return {
        "days": days,
        "total_checkins": total,
        "avg_feeling": round(avg, 2),
        "good_days": good,
        "ok_days": ok,
        "bad_days": bad,
    }


@router.get("/api/parents/{parent_id}/medicine-logs", response_model=list[MedicineLogResponse])
def list_medicine_logs(
    parent_id: int,
    days: int = Query(7, ge=1, le=365),
    db: Session = Depends(get_db),
):
    _assert_parent(parent_id, db)
    since = date.today() - timedelta(days=days)
    return (
        db.query(MedicineLog)
        .filter(MedicineLog.parent_id == parent_id, MedicineLog.scheduled_date >= since)
        .order_by(MedicineLog.scheduled_date.desc())
        .all()
    )


@router.get("/api/parents/{parent_id}/medicine-logs/summary")
def medicine_log_summary(
    parent_id: int,
    days: int = Query(7, ge=1, le=365),
    db: Session = Depends(get_db),
):
    _assert_parent(parent_id, db)
    since = date.today() - timedelta(days=days)
    logs = (
        db.query(MedicineLog)
        .filter(MedicineLog.parent_id == parent_id, MedicineLog.scheduled_date >= since)
        .all()
    )
    total = len(logs)
    taken = sum(1 for l in logs if l.taken)
    adherence = round((taken / total) * 100, 1) if total > 0 else 0

    return {
        "days": days,
        "total_scheduled": total,
        "total_taken": taken,
        "adherence_percent": adherence,
    }


def _assert_parent(parent_id: int, db: Session):
    if not db.query(Parent).filter(Parent.id == parent_id).first():
        raise HTTPException(404, "Parent not found")
