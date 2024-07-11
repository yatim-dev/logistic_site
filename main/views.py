from django.shortcuts import render

from .forms import UserInputForm
from .models import Order


def home(request):
    orders = []
    message = ''
    if request.method == 'POST':
        order_id = request.POST.get('string')
        orders = Order.objects.filter(uuid=order_id)
        if len(orders) == 0:
            message = 'Предупреждение: Заказ не найден!'

    context = {
        'form': UserInputForm(),
        'orders': orders,
        'message': message
    }
    return render(request, "main/home.html", context)



def about(request):
    return render(request, "main/about.html")


def support(request):
    return render(request, "main/support.html")