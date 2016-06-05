from django.shortcuts import render
from django.template import loader
from uuid import uuid4

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
def add(request):
    try:
        marketplace = request.POST['marketplace']
        amount = request.POST['amount']
        commission = request.POST['commission']
        purchaseDate = request.POST['purchaseDate']

    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'add.html', {
            'error_message': "one or more input are empty.",
        })
    else:
        O = Order.objects.create(order_id=uuid4(), marketplace=marketplace, order_amount =amount, order_commission=commission, order_purchase_date=purchaseDate)
        list_order = Order.objects.all()
        return render(request, 'list.html', {'list_order': list_order, 'detail': False})
