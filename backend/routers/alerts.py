from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from database import get_db
from models import Alert, Parent
from schemas import AlertResponse

router = APIRouter(tags=["Alerts"])


@router.get("/api/parents/{parent_id}/alerts", response_model=list[AlertResponse])
def list_alerts(parent_id: int, db: Session = Depends(get_db)):
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        raise HTTPException(404, "Parent not found")
    return (
        db.query(Alert)
        .filter(Alert.parent_id == parent_id)
        .order_by(Alert.created_at.desc())
        .limit(50)
        .all()
    )


@router.put("/api/alerts/{alert_id}/resolve", response_model=AlertResponse)
def resolve_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(404, "Alert not found")
    alert.resolved = True
    alert.resolved_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(alert)
    return alert
