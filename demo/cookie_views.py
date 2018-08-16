from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect


def list_cookies(request):
    return render(request, 'list_cookies.html',
                  {'cookies': request.COOKIES})


def add_cookie(request):
    if request.method == "GET":
        return render(request, 'add_cookie.html')
    else:
        # process data
        name = request.POST["cookie_name"]
        value = request.POST["cookie_value"]
        response = HttpResponseRedirect("/demo/list_cookies/")
        if 'durable' in request.POST:
            response.set_cookie(name, value,
                    expires=datetime.datetime.now() + datetime.timedelta(days=10))
        else:
            response.set_cookie(name, value)

    return response
