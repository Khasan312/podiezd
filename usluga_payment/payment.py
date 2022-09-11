import json
from datetime import datetime

import requests
from decouple import config

URL = "https://billing.crm.mycloud.kg/pay/main.php"
TOKEN = config("CRM_TOKEN", default="")


def make_payment(account_number, amount):
    """
    Make a payment request
    """

    data = {
        "token": TOKEN,
        "account_number": account_number,
        "refill_date_time": datetime.now(),
        "amount": amount,
        "action": "pay",
    }

    response = requests.post(URL, json.dumps(data, default=str))
    response_content = json.loads(response.text)

    return response_content


def check_account(account_number: int):
    data = {
        "token": TOKEN,
        "account_number": account_number,
        "action": "check",
    }

    response = requests.post(URL, json.dumps(data, default=str))
    response_content = json.loads(response.content)

    return response_content
