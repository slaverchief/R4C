from django.urls import path

from orders.views import make_order

urlpatterns = [
    path('', make_order),
]