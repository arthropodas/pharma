from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from datetime import datetime, timedelta, timezone
from decouple import config
import uuid
import jwt

def send_email(mail, subject, template, url,user_name, data=None):
    print("hiiii...")
    final_url = settings.BASE_URL + url
    link_to_send = {"url": final_url}
    app_name = settings.APP_NAME
    token_expiry = settings.RESET_TOKEN_EXPIRY
    
    if data is not None:
        context = {
            **link_to_send,
            **data,
            "app_name": app_name,
            "user_name": user_name,
            "token_expiry": token_expiry,
        }
    else:
        context = {**link_to_send, "app_name": app_name,"user_name": user_name}
    print("hello")
    from_email = f"<{settings.EMAIL_HOST}>"
    html = get_template(template)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, "", from_email, [mail])
    msg.attach_alternative(html_content, "text/html")
    print("msg..........",msg)
    msg.send()
def generate_reset_token(email, user_id):
    token_expiry_minutes = int(config("RESET_TOKEN_EXPIRY", default=1))
    exp = datetime.now(timezone.utc) + timedelta(minutes=token_expiry_minutes)
    jti = str(uuid.uuid4())
    payload = {
        "email": email,
        "user_id": user_id,
        "exp": exp,
        "token_type": "reset_password",
        "jti": jti,
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token