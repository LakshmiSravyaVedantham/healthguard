"""Twilio outbound WhatsApp message helper."""

import logging
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

logger = logging.getLogger(__name__)


def send_whatsapp(to_phone: str, message: str):
    """Send a WhatsApp message via Twilio."""
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        logger.warning(f"Twilio not configured. Would send to {to_phone}: {message[:80]}...")
        return None

    try:
        from twilio.rest import Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{to_phone}",
            body=message,
        )
        logger.info(f"Sent WhatsApp to {to_phone}: SID={msg.sid}")
        return msg.sid
    except Exception as e:
        logger.error(f"Failed to send WhatsApp to {to_phone}: {e}")
        return None
