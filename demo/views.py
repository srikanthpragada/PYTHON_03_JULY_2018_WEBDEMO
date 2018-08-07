from django.shortcuts import render
from . models import Info
from datetime import datetime
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',
                  {
                    "info" : Info(),
                    "now" : str(datetime.now())
                  }
                )
