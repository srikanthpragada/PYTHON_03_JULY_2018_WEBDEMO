from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect

def add_key(request):
    message  = ""
    if 'key' in request.GET:
        key = request.GET['key']
        value = request.GET['value']
        request.session[key] = value
        message = "Added Key!"

    return render(request,'sessions.html', {'message' : message} )


def list_keys(request):
    return render(request,'list_keys.html', {'data' : request.session })