"""APScheduler cron jobs for medicine reminders, health tips, and exercise suggestions."""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal
from models import Parent, Medicine
from services.message_sender import send_whatsapp
from services.translations import get_message
from services.health_tips import get_random_tip

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")


def start_scheduler():
    """Start all scheduled reminder jobs."""
    # 7:00 AM - Good morning + health tip
    scheduler.add_job(morning_greeting_job, "cron", hour=7, minute=0, id="morning_greeting")

    # 8:00 AM - Morning medicine reminder
    scheduler.add_job(medicine_reminder_job, "cron", hour=8, minute=0,
                      id="morning_medicine", args=["morning"])

    # 12:30 PM - Afternoon medicine reminder
    scheduler.add_job(medicine_reminder_job, "cron", hour=12, minute=30,
                      id="afternoon_medicine", args=["afternoon"])

    # 3:00 PM - Hydration reminder
    scheduler.add_job(hydration_reminder_job, "cron", hour=15, minute=0, id="hydration")

    # 6:00 PM - Evening exercise suggestion
    scheduler.add_job(exercise_reminder_job, "cron", hour=18, minute=0, id="exercise")

    # 9:00 PM - Night medicine + daily check-in
    scheduler.add_job(night_checkin_job, "cron", hour=21, minute=0, id="night_checkin")

    scheduler.start()
    logger.info("Reminder scheduler started with 6 daily jobs (IST)")


def _get_active_parents():
    """Get all active parents from the database."""
    db = SessionLocal()
    try:
        return db.query(Parent).filter(Parent.active == True, Parent.name != "").all()
    finally:
        db.close()


def morning_greeting_job():
    """Send good morning + health tip to all active parents."""
    parents = _get_active_parents()
    for parent in parents:
        greeting = get_message("morning_greeting", parent.language, name=parent.name)
        tip_prefix = get_message("health_tip_prefix", parent.language)
        tip = get_random_tip(parent.language)
        message = greeting + "\n\n" + tip_prefix + tip
        send_whatsapp(parent.phone, message)
    logger.info(f"Morning greeting sent to {len(parents)} parents")


def medicine_reminder_job(time_slot: str):
    """Send medicine reminder for a specific time slot."""
    db = SessionLocal()
    try:
        parents = db.query(Parent).filter(Parent.active == True, Parent.name != "").all()
        for parent in parents:
            medicines = (
                db.query(Medicine)
                .filter(
                    Medicine.parent_id == parent.id,
                    Medicine.active == True,
                    Medicine.time_slot == time_slot,
                )
                .all()
            )
            if medicines:
                reminder = get_message("medicine_reminder", parent.language,
                                       name=parent.name, time_slot=time_slot)
                med_list = "\n".join(
                    f"• {m.name_telugu or m.name} - {m.dosage}" for m in medicines
                )
                confirm = get_message("medicine_confirm", parent.language)
                send_whatsapp(parent.phone, reminder + "\n\n" + med_list + confirm)
        logger.info(f"Medicine reminder ({time_slot}) sent")
    finally:
        db.close()


def hydration_reminder_job():
    """Send hydration reminder."""
    parents = _get_active_parents()
    for parent in parents:
        msg = get_message("hydration_reminder", parent.language, name=parent.name)
        send_whatsapp(parent.phone, msg)
    logger.info(f"Hydration reminder sent to {len(parents)} parents")


def exercise_reminder_job():
    """Send evening exercise suggestion."""
    parents = _get_active_parents()
    for parent in parents:
        msg = get_message("exercise_reminder", parent.language, name=parent.name)
        send_whatsapp(parent.phone, msg)
    logger.info(f"Exercise reminder sent to {len(parents)} parents")


def night_checkin_job():
    """Send night medicine reminder + check-in prompt."""
    db = SessionLocal()
    try:
        parents = db.query(Parent).filter(Parent.active == True, Parent.name != "").all()
        for parent in parents:
            # Night medicine reminder
            medicines = (
                db.query(Medicine)
                .filter(
                    Medicine.parent_id == parent.id,
                    Medicine.active == True,
                    Medicine.time_slot == "night",
                )
                .all()
            )
            parts = []
            if medicines:
                parts.append(
                    get_message("medicine_reminder", parent.language,
                                name=parent.name, time_slot="night")
                )
                parts.append("\n".join(f"• {m.name_telugu or m.name} - {m.dosage}" for m in medicines))

            parts.append(get_message("night_checkin_reminder", parent.language, name=parent.name))
            send_whatsapp(parent.phone, "\n\n".join(parts))
        logger.info(f"Night check-in sent to {len(parents)} parents")
    finally:
        db.close()
