from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
import requests
from django.shortcuts import render
from usluga_payment.models import Podiezd, BaipInfo
from usluga_payment.templates.python import js_file, html

        # 'cashregister_id': ['10300103'], 'kiosk_id': ['724300'], 'receipt_id': ['438'], 'productcode': ['2280001003660'], 'language': ['ru'], 'partner_id': ['513744']

def index(request):
    request_info = dict(request.GET)

    info = BaipInfo.objects.filter(
        cashregister_id= request_info['cashregister_id'][0],
        kiosk_id= request_info['kiosk_id'][0],
        receipt_id =request_info['receipt_id'][0],
        partner_id= request_info['partner_id'][0]
    )

    if not info.exists():
        BaipInfo.objects.create(
            cashregister_id= request_info['cashregister_id'][0],
            kiosk_id= request_info['kiosk_id'][0],
            receipt_id =request_info['receipt_id'][0],
            partner_id= request_info['partner_id'][0]
        )
    print(info.exists())
        

    js_main = js_file(10300103, 724300, 420, 2280007001455, 513744, 1000, "2022-10-07T18:04:15", "T%2fQ82UIrla8p365frh9ozAyz7OZ0g7%2bFTnEJV1PHRgkgVgLqvyIeFLnutKlAo6lBdmGi6RciIJUmJm1fDjzJXXU4%2bE7KqvTnGQe3aH2lHnL54gHeKSuJpKKeVjcV9cSjhDdCFxuqBM2wBdTBGJOsRCqqkrf%2fie9AusoF%2f0LUCCs%3d")
    
    return HttpResponse (html(js_main))
