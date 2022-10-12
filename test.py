URL = "http://192.168.181.2/Operator.ashx"
from decouple import config

import requests
import json
import xmltodict

# TOKEN = config("CRM_TOKEN", default="")

# data = {
#         "token": TOKEN,
#         "account_number": 123456789,
#         "action": "check",
#     }

response = requests.get(URL)
print(response.content)
response_content = xmltodict.parse(response.text)
print(response_content)
