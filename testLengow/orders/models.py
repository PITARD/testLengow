from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=200, primary_key=True)
    marketplace = models.CharField(max_length=30)
    order_purchase_date = models.DateTimeField()
    order_amout = models.FloatField()
    order_commission = models.FloatField()
