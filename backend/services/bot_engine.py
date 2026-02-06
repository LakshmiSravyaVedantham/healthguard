"""Conversation state machine - the core brain of the WhatsApp bot."""

from datetime import date, datetime, timezone
from sqlalchemy.orm import Session
from models import Parent, Medicine, HealthCheckin, MedicineLog, Alert
from services.translations import get_message
from services.health_tips import get_random_tip


# Conversation states
STATE_NEW = "new"
STATE_ONBOARD_LANG = "onboard_lang"
STATE_ONBOARD_NAME = "onboard_name"
STATE_ONBOARD_AGE = "onboard_age"
STATE_MAIN_MENU = "main_menu"
STATE_MEDICINE_CHECK = "medicine_check"
STATE_CHECKIN_FEELING = "checkin_feeling"
STATE_CHECKIN_SYMPTOM = "checkin_symptom"
STATE_EXERCISE_MENU = "exercise_menu"
STATE_EMERGENCY = "emergency"
STATE_LANGUAGE_CHANGE = "language_change"


def process_message(phone: str, body: str, db: Session) -> str:
    """Process an incoming WhatsApp message and return a reply."""
    body = body.strip()

    parent = db.query(Parent).filter(Parent.phone == phone).first()

    # New user - start onboarding
    if parent is None:
        return _handle_new_user(phone, db)

    # Always allow "0" to go back to menu
    if body == "0":
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("main_menu", parent.language)

    state = parent.conversation_state or STATE_MAIN_MENU

    handlers = {
        STATE_NEW: _handle_new_user_existing,
        STATE_ONBOARD_LANG: _handle_onboard_lang,
        STATE_ONBOARD_NAME: _handle_onboard_name,
        STATE_ONBOARD_AGE: _handle_onboard_age,
        STATE_MAIN_MENU: _handle_main_menu,
        STATE_MEDICINE_CHECK: _handle_medicine_check,
        STATE_CHECKIN_FEELING: _handle_checkin_feeling,
        STATE_CHECKIN_SYMPTOM: _handle_checkin_symptom,
        STATE_EXERCISE_MENU: _handle_exercise_menu,
        STATE_EMERGENCY: _handle_emergency,
        STATE_LANGUAGE_CHANGE: _handle_language_change,
    }

    handler = handlers.get(state, _handle_main_menu)
    return handler(parent, body, db)


def _handle_new_user(phone: str, db: Session) -> str:
    """Create a new parent record and start onboarding."""
    parent = Parent(
        phone=phone,
        name="",
        language="both",
        conversation_state=STATE_ONBOARD_LANG,
    )
    db.add(parent)
    db.commit()
    return get_message("welcome", "both")


def _handle_new_user_existing(parent: Parent, body: str, db: Session) -> str:
    parent.conversation_state = STATE_ONBOARD_LANG
    db.commit()
    return get_message("welcome", "both")


def _handle_onboard_lang(parent: Parent, body: str, db: Session) -> str:
    lang_map = {"1": "telugu", "2": "english", "3": "both"}
    if body in lang_map:
        parent.language = lang_map[body]
        parent.conversation_state = STATE_ONBOARD_NAME
        db.commit()
        return get_message("ask_name", parent.language)
    return get_message("welcome", "both")


def _handle_onboard_name(parent: Parent, body: str, db: Session) -> str:
    if len(body) < 2 or body.isdigit():
        return get_message("ask_name", parent.language)
    parent.name = body.title()
    parent.conversation_state = STATE_ONBOARD_AGE
    db.commit()
    return get_message("ask_age", parent.language)


def _handle_onboard_age(parent: Parent, body: str, db: Session) -> str:
    if not body.isdigit() or not (20 <= int(body) <= 120):
        return get_message("ask_age", parent.language)
    parent.age = int(body)
    parent.conversation_state = STATE_MAIN_MENU
    db.commit()
    return get_message("onboarding_complete", parent.language, name=parent.name)


def _handle_main_menu(parent: Parent, body: str, db: Session) -> str:
    menu_handlers = {
        "1": _show_exercise_menu,     # Exercise first!
        "2": _show_health_tip,
        "3": _show_checkin,
        "4": _show_medicine_check,
        "5": _show_emergency,
        "6": _show_language_change,
    }
    handler = menu_handlers.get(body)
    if handler:
        return handler(parent, db)
    return get_message("main_menu", parent.language)


def _show_health_tip(parent: Parent, db: Session) -> str:
    prefix = get_message("health_tip_prefix", parent.language)
    tip = get_random_tip(parent.language)
    footer = "\n\n0 - " + ("Menu" if parent.language == "english" else "Menu ki vellandi")
    return prefix + tip + footer


def _show_medicine_check(parent: Parent, db: Session) -> str:
    medicines = (
        db.query(Medicine)
        .filter(Medicine.parent_id == parent.id, Medicine.active == True)
        .all()
    )
    if not medicines:
        return get_message("no_medicines", parent.language)

    header = get_message("medicine_list_header", parent.language)
    lines = []
    for m in medicines:
        name_display = f"{m.name}"
        if m.name_telugu and parent.language in ("telugu", "both"):
            name_display = f"{m.name_telugu} ({m.name})"
        time_str = m.time_exact or m.time_slot
        lines.append(f"• {name_display} - {m.dosage} - {time_str}")

    confirm = get_message("medicine_confirm", parent.language)
    parent.conversation_state = STATE_MEDICINE_CHECK
    db.commit()
    return header + "\n".join(lines) + confirm


def _handle_medicine_check(parent: Parent, body: str, db: Session) -> str:
    medicines = (
        db.query(Medicine)
        .filter(Medicine.parent_id == parent.id, Medicine.active == True)
        .all()
    )

    if body == "1":
        # Done — auto-log all as taken
        for m in medicines:
            _record_medicine_log(parent.id, m.id, m.time_slot, True, db)
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("medicine_all_taken", parent.language)
    else:
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("main_menu", parent.language)


def _show_checkin(parent: Parent, db: Session) -> str:
    parent.conversation_state = STATE_CHECKIN_FEELING
    db.commit()
    return get_message("checkin_feeling", parent.language)


def _handle_checkin_feeling(parent: Parent, body: str, db: Session) -> str:
    if body not in ("1", "2", "3"):
        return get_message("checkin_feeling", parent.language)

    feeling = int(body)
    today = date.today()

    # Check for existing checkin today and update or create
    existing = (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent.id, HealthCheckin.checkin_date == today)
        .first()
    )
    if existing:
        existing.feeling = feeling
    else:
        checkin = HealthCheckin(parent_id=parent.id, checkin_date=today, feeling=feeling)
        db.add(checkin)

    if feeling == 1:
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("checkin_good", parent.language)
    elif feeling == 2:
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("checkin_ok", parent.language)
    else:
        parent.conversation_state = STATE_CHECKIN_SYMPTOM
        db.commit()
        return get_message("checkin_bad_symptoms", parent.language)


def _handle_checkin_symptom(parent: Parent, body: str, db: Session) -> str:
    symptoms = {
        "1": "Headache",
        "2": "Dizziness",
        "3": "Breathing difficulty",
        "4": "Joint pain",
        "5": "Vision problems",
        "6": "Other",
    }
    if body not in symptoms:
        return get_message("checkin_bad_symptoms", parent.language)

    symptom = symptoms[body]
    today = date.today()
    checkin = (
        db.query(HealthCheckin)
        .filter(HealthCheckin.parent_id == parent.id, HealthCheckin.checkin_date == today)
        .first()
    )
    if checkin:
        checkin.notes = symptom

    # Severe symptoms that trigger urgent alert
    severe = body in ("2", "3")  # dizziness, breathing
    alert_type = "health_severe" if severe else "health_bad"
    msg = f"{parent.name} reported feeling bad: {symptom}"
    _create_alert(parent.id, alert_type, msg, db)

    parent.conversation_state = STATE_MAIN_MENU
    db.commit()

    if severe:
        return get_message("checkin_severe_alert", parent.language)
    return get_message("checkin_symptom_recorded", parent.language)


def _show_exercise_menu(parent: Parent, db: Session) -> str:
    parent.conversation_state = STATE_EXERCISE_MENU
    db.commit()
    return get_message("exercise_menu", parent.language)


def _handle_exercise_menu(parent: Parent, body: str, db: Session) -> str:
    exercises = {
        "1": "exercise_chair_yoga",
        "2": "exercise_walking",
        "3": "exercise_pranayama",
        "4": "exercise_eyes",
    }
    if body in exercises:
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        msg = get_message(exercises[body], parent.language)
        footer = "\n\n0 - " + ("Menu" if parent.language == "english" else "Menu ki vellandi")
        return msg + footer
    return get_message("exercise_menu", parent.language)


def _show_emergency(parent: Parent, db: Session) -> str:
    family_contact = ""
    if parent.emergency_contact_phone:
        family_contact = f"👨‍👩‍👦 Family: {parent.emergency_contact_phone}"

    parent.conversation_state = STATE_EMERGENCY
    db.commit()
    return get_message("emergency_info", parent.language, family_contact=family_contact)


def _handle_emergency(parent: Parent, body: str, db: Session) -> str:
    if body == "1":
        _create_alert(parent.id, "sos", f"🆘 SOS from {parent.name}!", db)
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("sos_sent", parent.language)
    parent.conversation_state = STATE_MAIN_MENU
    db.commit()
    return get_message("main_menu", parent.language)


def _show_language_change(parent: Parent, db: Session) -> str:
    parent.conversation_state = STATE_LANGUAGE_CHANGE
    db.commit()
    return get_message("language_change", parent.language)


def _handle_language_change(parent: Parent, body: str, db: Session) -> str:
    lang_map = {"1": "telugu", "2": "english", "3": "both"}
    if body in lang_map:
        parent.language = lang_map[body]
        parent.conversation_state = STATE_MAIN_MENU
        db.commit()
        return get_message("language_changed", parent.language)
    return get_message("language_change", parent.language)


def _record_medicine_log(parent_id: int, medicine_id: int, time_slot: str,
                         taken: bool, db: Session):
    """Record whether a medicine was taken."""
    today = date.today()
    existing = (
        db.query(MedicineLog)
        .filter(
            MedicineLog.parent_id == parent_id,
            MedicineLog.medicine_id == medicine_id,
            MedicineLog.scheduled_date == today,
            MedicineLog.time_slot == time_slot,
        )
        .first()
    )
    if existing:
        existing.taken = taken
        if taken:
            existing.confirmed_at = datetime.now(timezone.utc)
    else:
        log = MedicineLog(
            parent_id=parent_id,
            medicine_id=medicine_id,
            scheduled_date=today,
            time_slot=time_slot,
            taken=taken,
            confirmed_at=datetime.now(timezone.utc) if taken else None,
        )
        db.add(log)


def _create_alert(parent_id: int, alert_type: str, message: str, db: Session):
    """Create an alert for the family."""
    alert = Alert(
        parent_id=parent_id,
        alert_type=alert_type,
        message=message,
    )
    db.add(alert)
