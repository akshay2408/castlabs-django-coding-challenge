from datetime import datetime, timedelta

from django.db.models import Q
from django.shortcuts import HttpResponse
from licenses.task import email_notification

from .models import License


def get_clients_info():
    current_datetime = datetime.utcnow()
    four_months_previous = current_datetime - timedelta(days=120)
    month_end_date = current_datetime + timedelta(days=30)
    week_end_date = current_datetime + timedelta(days=7)

    # 
    licenses_obj = License.objects.filter(
        Q(expiration_datetime=four_months_previous)
        | Q(expiration_datetime__date__range=[current_datetime, month_end_date],
            expiration_datetime__week_day=1)
        | Q(expiration_datetime__range=[current_datetime, week_end_date]))

    for license in licenses_obj:
        clients_email = license.client.admin_poc.email
        success = email_notification.delay(clients_email)
    return success


def index(request):
    get_clients_info()
    return HttpResponse("success")