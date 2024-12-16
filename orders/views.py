from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Order
from robots.models import Robot
from customers.models import Customer
import json

# Создание заказа
def make_order(request):
    data = json.loads(request.body)
    email = data['email']
    serial = data['serial']
    c = None
    try:
        c = Customer.objects.get(email=email)
    except ObjectDoesNotExist:
        c = Customer.objects.create(email=email)
    rob = Robot.objects.filter(serial=serial)
    if not rob:
        Order.objects.create(customer=c, robot_serial=serial, in_waiting=True)
    else:
        Order.objects.create(customer=c, robot_serial=serial)
    return HttpResponse("success")