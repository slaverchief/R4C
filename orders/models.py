from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5,blank=False, null=False)
    in_waiting = models.BooleanField(default=False) # Определяет, сделан заказ на существующего робота(False) или на робота, о создании которого надо уведомить пользователя(True)
