from datetime import datetime

import requests
from django.shortcuts import render
from usluga_payment.models import Podiezd


def index(request):
    return render(request, "index.html")
