from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect

movies = {
    "vizag": ['Abc', 'Xyz', 'Pqr'],
    "Hyderabad": ['Def', 'XXyy', 'Abcd'],
    "Chennai": ['ZZZ', 'ADE', 'PQR', 'HIJ'],
    'Mumbai': ['uueueu']
}


def list_movies(request):
    if 'city' in request.COOKIES:
        city = request.COOKIES['city']
        return render(request, 'list_movies.html',
                      {'city': city,
                       'movies': movies[city]
                       }
                      )
    else:
        return HttpResponseRedirect('/demo/selectcity')


def select_city(request):
    return render(request, 'select_city.html', {'cities': movies.keys()})


def save_city(request):
    response = HttpResponseRedirect("/demo/movies")
    response.set_cookie("city", request.GET["city"],
                        expires=datetime.datetime.now() +
                                datetime.timedelta(days=10))
    return response


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
