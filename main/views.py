from django.shortcuts import render, redirect
from validate_email import validate_email
from .forms import UserInputForm, SupportForm
from .models import Order
from django.contrib import messages


def home(request):
    orders = []
    error_message = ''
    if request.method == 'POST':
        order_id = request.POST.get('string')
        orders = Order.objects.filter(uuid=order_id)
        if len(orders) == 0:
            error_message = 'Предупреждение: Заказ не найден!'

    context = {
        'form': UserInputForm(),
        'orders': orders,
        'error_message': error_message
    }
    return render(request, "main/home.html", context)


def about(request):
    return render(request, "main/about.html")


def support(request):
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        if validate_email(email):
            print(email, title, message)
            messages.success(request, 'Сообщение доставлено')
        else:
            error_message = 'Предупреждение: неверно указана почта'

    content = {
        'form': SupportForm(),
        'error_message': error_message
    }
    return render(request, "main/support.html", content)
