from django.shortcuts import render
from django.template import loader
from uuid import uuid4
from rest_framework import viewsets

from .serializers import OrderSerializer
from .models import Order

def index(request):
    return render(request, 'index.html')
def list(request):
    list_order = Order.objects.all()
    return render(request, 'list.html', {'list_order': list_order, 'detail': False})
def detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'list.html', {'list_order': [order], 'detail': True})
def addOrders(request) :
    return render(request, 'add.html')
def modifOrders(request, order_id) :
    order = Order.objects.get(pk=order_id)
    return render(request, 'add.html', {'order':order})
def add(request):
    try:
        marketplace = request.POST['marketplace']
        amount = request.POST['amount']
        commission = request.POST['commission']
        purchaseDate = request.POST['purchaseDate']
        order_id = request.POST['order_id']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'add.html', {
            'error_message': "one or more input are empty.",
        })
    else:
        try:
            O = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            O = Order.objects.create(order_id=uuid4(), marketplace=marketplace, order_amount =amount, order_commission=commission, order_purchase_date=purchaseDate)
        else:
            O.marketplace = marketplace
            O.order_amount = amount
            O.order_commission = commission
            O.order_purchase_date = purchaseDate
            O.save()
        list_order = Order.objects.all()
        return render(request, 'list.html', {'list_order': list_order, 'detail': False})

class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
