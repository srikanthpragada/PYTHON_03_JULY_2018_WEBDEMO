from django.http import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def today(request):
    now = datetime.now()
    return HttpResponse("<h2>" + str(now) + "</h2>")


def wish(request):
    name = request.GET.get("name","Unknown")

    now = datetime.now()
    message = "Good Evening"
    if now.hour < 12:
        message = "Good Morning"
    elif now.hour < 17:
        message = "Good Afternoon"

    return HttpResponse("<h2>%s to  %s </h2>" % (message,name))
