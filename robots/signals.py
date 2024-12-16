from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Robot
from django.core.mail import send_mail
from orders.models import Order

# Сигнал, срабатывающий при создании робота. Отправляет сообщение, если робота ожидают в заказах.
@receiver(post_save, sender=Robot)
def notification_email(sender, instance, created, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial)
    if not orders:
        return
    message = f"Добрый день! \
Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. \
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"
    send_mail("Уведомление о появлении робота", message, settings.EMAIL_HOST_USER, [orders[0].customer.email], fail_silently=False)
    orders[0].in_waiting = False