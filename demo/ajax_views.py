from django.shortcuts import render, redirect
import datetime
import time
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def index(request):
    return render(request, 'ajax_index.html')


def now(request):
    # time.sleep(10)
    return HttpResponse(str(datetime.datetime.now()))
