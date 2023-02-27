from celery import shared_task
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from licenses.models import License


@shared_task()
def email_notification(recipients: str):
    """ A convenience method to send email notifications
    """
    subject = 'Notification Alert'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = recipients

    license_obj = License.objects.select_related('client').filter(client__admin_poc__email=recipients)    
    
    html_message = render_to_string('email.html', {'context': license_obj})
    plain_message = strip_tags(html_message)

    try:
        mail.send_mail(subject, plain_message, email_from, [recipient_list], html_message=html_message)
    except Exception as e:
        print(str(e))
    return True