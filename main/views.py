from django.shortcuts import render

from .forms import UserInputForm
from .models import Order


def home(request):
    orders = []
    if request.method == 'POST':
        order_id = request.POST.get('string')
        orders = Order.objects.filter(uuid=order_id)
        print(orders)

    context = {
        'form': UserInputForm(),
        'orders': orders
    }
    return render(request, "main/home.html", context)


def about(request):
    return render(request, "main/about.html")
