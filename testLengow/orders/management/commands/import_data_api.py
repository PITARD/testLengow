from django.core.management.base import BaseCommand, CommandError
from orders.models import Order
from xml.dom import minidom

import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        doc = minidom.parse('Y:/testLengow/testLengow/orders/management/commands/orders-test.xml')
        orders = doc.getElementsByTagName("order")
        for order in orders:
            order_id = order.getElementsByTagName("order_id")[0]
            marketplace = order.getElementsByTagName("marketplace")[0]
            order_amount = order.getElementsByTagName("order_amount")[0]
            order_commission = order.getElementsByTagName("order_commission")[0]
            order_purchase_date = order.getElementsByTagName("order_purchase_date")[0]
            try:
                order_purchase_date_data = order_purchase_date.firstChild.data
            except AttributeError:
                order_purchase_date_data = datetime.datetime.now();
            O = Order.objects.create(order_id=order_id.firstChild.data, marketplace=marketplace.firstChild.data, order_amount=order_amount.firstChild.data,
            order_commission=order_commission.firstChild.data, order_purchase_date=order_purchase_date_data)
