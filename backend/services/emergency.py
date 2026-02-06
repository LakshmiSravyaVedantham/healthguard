"""SOS alerts and emergency contact handling."""

import logging
from sqlalchemy.orm import Session
from models import Parent, FamilyMember, Alert
from services.message_sender import send_whatsapp
from services.translations import get_message

logger = logging.getLogger(__name__)


def send_sos_alert(parent_id: int, db: Session):
    """Send SOS alert to family members and emergency contact."""
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        return

    alert_msg_telugu = (
        f"🆘 *EMERGENCY ALERT*\n\n"
        f"{parent.name} gaaru SOS pampaaru!\n"
        f"Phone: {parent.phone}\n"
        f"Velluduga check cheyandi leda call cheyandi."
    )
    alert_msg_english = (
        f"🆘 *EMERGENCY ALERT*\n\n"
        f"{parent.name} has sent an SOS alert!\n"
        f"Phone: {parent.phone}\n"
        f"Please check on them immediately or call."
    )

    # Send to emergency contact
    if parent.emergency_contact_phone:
        send_whatsapp(parent.emergency_contact_phone, alert_msg_english)
        logger.info(f"SOS sent to emergency contact: {parent.emergency_contact_phone}")

    # Send to all family members
    family_members = (
        db.query(FamilyMember)
        .filter(FamilyMember.parent_id == parent_id)
        .all()
    )
    for fm in family_members:
        if fm.phone:
            send_whatsapp(fm.phone, alert_msg_english)
            logger.info(f"SOS sent to family member: {fm.name} ({fm.phone})")

    # Create alert record
    alert = Alert(
        parent_id=parent_id,
        alert_type="sos",
        message=f"SOS Alert from {parent.name}",
    )
    db.add(alert)
    db.commit()


def send_health_alert(parent_id: int, symptom: str, severity: str, db: Session):
    """Send health alert to family when parent reports feeling bad."""
    parent = db.query(Parent).filter(Parent.id == parent_id).first()
    if not parent:
        return

    severity_label = "URGENT" if severity == "severe" else "Alert"
    alert_msg = (
        f"⚠️ *Health {severity_label}*\n\n"
        f"{parent.name} is not feeling well.\n"
        f"Symptom: {symptom}\n"
        f"Severity: {severity}\n"
        f"Phone: {parent.phone}\n"
        f"Please check on them."
    )

    if parent.emergency_contact_phone:
        send_whatsapp(parent.emergency_contact_phone, alert_msg)

    family_members = (
        db.query(FamilyMember)
        .filter(FamilyMember.parent_id == parent_id)
        .all()
    )
    for fm in family_members:
        if fm.phone:
            send_whatsapp(fm.phone, alert_msg)


EMERGENCY_NUMBERS = {
    "ambulance": {"number": "108", "telugu": "Ambulance", "english": "Ambulance"},
    "health_helpline": {"number": "104", "telugu": "Health Helpline", "english": "Health Helpline"},
    "police": {"number": "100", "telugu": "Police", "english": "Police"},
    "fire": {"number": "101", "telugu": "Fire Brigade", "english": "Fire Brigade"},
    "women_helpline": {"number": "181", "telugu": "Women Helpline", "english": "Women Helpline"},
    "senior_citizen": {"number": "14567", "telugu": "Senior Citizen Helpline", "english": "Senior Citizen Helpline"},
}
