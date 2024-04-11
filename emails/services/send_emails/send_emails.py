from app import settings
from django.template import Context, Template
from django.core.mail import EmailMessage
from django.template.loader import get_template


class SendEmail:
    def __init__(self, subscription) -> None:
        self.subscription = subscription

    def render_context(self):
        template_path = "emails/services/send_emails/template.html"
        with open(template_path, "r") as file:
            template_content = file.read()
        template = Template(template_content)
        context = Context({
            "name": self.subscription["name"],
        })

        return template.render(context)

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
