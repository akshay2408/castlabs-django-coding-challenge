from django.conf import settings
from django.core.mail import send_mail
from django.template import Template
from django.template.loader import get_template, render_to_string
from licenses.models import License


class EmailNotification:
    """ A convenience class to send email notifications
    """
    subject = "Email Notification"  # type: str
    from_email = settings.DEFAULT_FROM_EMAIL  # type: str
    template_path = 'email.html'  # type: str

    @classmethod
    def load_template(cls) -> Template:
        """Load the configured template path"""
        return get_template(cls.template_path)

    @classmethod
    # @shared_task
    def send_notification(cls, recipients: str):
        """Send the notification using the given context"""
        template = cls.load_template()
        message_body = template.render(context={})
        license_obj = License.objects.select_related('client').filter(
            client__admin_poc__email=recipients)    
        html_message = render_to_string('email.html', {'context': license_obj})
        send_mail(cls.subject, message_body, cls.from_email,
                   [recipients], html_message=html_message)