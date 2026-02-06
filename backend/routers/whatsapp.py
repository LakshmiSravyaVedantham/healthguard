from fastapi import APIRouter, Request, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from database import get_db
from services.bot_engine import process_message

router = APIRouter(tags=["WhatsApp"])


@router.post("/webhook/whatsapp", response_class=PlainTextResponse)
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    """Handle incoming WhatsApp messages from Twilio."""
    form = await request.form()
    from_number = form.get("From", "")  # e.g. "whatsapp:+919876543210"
    body = form.get("Body", "").strip()

    # Extract phone number (remove "whatsapp:" prefix)
    phone = from_number.replace("whatsapp:", "").strip()

    if not phone or not body:
        return _twiml_response("Please send a message.")

    reply = process_message(phone, body, db)
    return _twiml_response(reply)


def _twiml_response(message: str) -> str:
    """Wrap reply in TwiML XML format for Twilio."""
    escaped = (
        message
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        "<Response>"
        f"<Message>{escaped}</Message>"
        "</Response>"
    )
