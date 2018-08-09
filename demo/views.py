from django.shortcuts import render
from .models import Info
from datetime import datetime
from django.http import HttpResponse
import requests


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
                   'message': message}
                  )


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    return render(request, 'list_countries.html', {'countries': countries})
