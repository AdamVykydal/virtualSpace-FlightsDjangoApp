from django.shortcuts import render

from .models import Customer

def index(request):
    return render(request, "flights/index.html", {
        "Customer": Customer.objects.all()
    })
