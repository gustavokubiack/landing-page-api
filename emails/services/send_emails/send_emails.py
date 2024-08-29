from app import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class SendEmail:
    def __init__(self, subscription) -> None:
        self.subscription = subscription

    def render_context(self):
        context = {
            "name": self.subscription["name"],
        }
        return render_to_string('emails/services/send_emails/template.html', context)

    def send(self):
        template = self.render_context()
        email = EmailMessage(
            subject="Confirmação de Inscrição | InovaTech Summit",
            from_email=settings.EMAIL_HOST_USER,
            body=template,
            to=[self.subscription["email"]],
        )
        email.content_subtype = "html"
        email.send()
