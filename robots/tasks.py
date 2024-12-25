from celery import shared_task
from django.core.mail import send_mail
from R4C import settings

@shared_task
def send_email_task(message, address):
    send_mail("Уведомление о появлении робота", message, settings.EMAIL_HOST_USER, [address], fail_silently=False)