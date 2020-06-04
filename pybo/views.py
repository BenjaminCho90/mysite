from django.shortcuts import render
from .models import Customer,Product,Order
# Create your views here.


def index(request):
    # pybo 목록 출력

    customer_list = Customer.objects.order_by('create_date')
    context = {'customer_list':customer_list}
    return render(request, 'pybo/customer_list.html', context)


def detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    context = {'customer': customer}
    return render(request, 'pybo/customer_detail.html', context)