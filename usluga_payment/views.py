from django.shortcuts import render
import requests
from .payment import make_post_payment
from .models import Podiezd
from datetime import datetime



def index(request):
    return render(request, "index.html")


def home(request):
    response = requests.get('https://billing.crm.mycloud.kg/pay/main.php').json()
    return render(request, 'home.html', {'response':response})


def json():
    url = 'https://billing.crm.mycloud.kg/pay/main.php'
    response = requests.get(url)
    data = response.json()['message']
    print(data)
    for i in (data):
        Podiezd.objects.create(account_number=data['account_number'], refill_date_time=i[datetime.now()], amount=i['amount'], action=i['check'])
        print(data)
