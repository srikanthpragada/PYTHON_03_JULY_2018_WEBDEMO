from django.shortcuts import render
from .models import Info
from datetime import datetime
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html',
                  {
                      "info": Info(),
                      "now": str(datetime.now())
                  }
                  )


def discount(request):
    discount = 0
    amount = ''
    rate = ''
    message = ""
    if request.method == "POST":
        try:
            amount = float(request.POST["amount"])
            rate = float(request.POST["rate"])
            discount = amount * rate / 100
        except:
            message = "Invalid Input. Please enter valid numbers for amount and rate!"

    return render(request, 'discount.html',
                  {'discount': discount,
                   'amount': amount,
                   'rate': rate,
                   'message' : message}
                 )
