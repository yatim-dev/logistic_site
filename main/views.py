from django.shortcuts import render
from .models import Order

# Create your views here.
def home(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, "main/home.html", context)


def about(request):
    return render(request, "main/about.html")
