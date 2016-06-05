import datetime

from django.db import models
from django.utils import timezone

class Order(models.Model):
    order_id = models.CharField(max_length=200, primary_key=True)
    marketplace = models.CharField(max_length=30)
    order_purchase_date = models.DateTimeField()
    order_amount = models.FloatField()
    order_commission = models.FloatField()
    def __str__(self):
        return self.order_id
    def last_order(self):
        return self.order_purchase_date >= timezone.now() - datetime.timedelta(days=1)
