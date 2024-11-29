from twilio.rest import Client
from django.conf import settings

def send_sms(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(
            to=to,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=message
        )
        return "Message sent successfully!"
    except Exception as e:
        return str(e)
