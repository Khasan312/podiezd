import json
from datetime import datetime

import requests

URL = "https://billing.crm.mycloud.kg/pay/main.php"


def post_payment(token, account_number, refil_date_time, amount, action):

    data = {
        "token": token,
        "account_number": account_number,
        "refill_date_time": refil_date_time,
        "amount": amount,
        "action": action,
    }
    return json.dumps(data, default=str)


def make_post_payment(token, account_number, refil_date_time, amount, action):

    info = post_payment(token, account_number, refil_date_time, amount, action)

    response = requests.post(URL, info)
    response_content = json.loads(response.text)

    return response_content


pay = make_post_payment(
    "yVKdAGWwCu6sb7j8CNjhiW7JeFv7CBlN", 123456789, datetime.now(), '500', "check"
)

print(pay)
