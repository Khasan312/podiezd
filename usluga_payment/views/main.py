from django.shortcuts import render

from usluga_payment.models import Operator


def index(request):
    request_info = dict(request.GET)

    operator = Operator.objects.filter(
        cashregister_id=request_info["cashregister_id"][0],
        kiosk_id=request_info["kiosk_id"][0],
        receipt_id=request_info["receipt_id"][0],
        partner_id=request_info["partner_id"][0],
    )

    if not operator.exists():
        Operator.objects.create(
            cashregister_id=request_info["cashregister_id"][0],
            kiosk_id=request_info["kiosk_id"][0],
            receipt_id=request_info["receipt_id"][0],
            partner_id=request_info["partner_id"][0],
        )

    return render(request, "home.html")
