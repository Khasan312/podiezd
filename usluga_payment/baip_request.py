import xml.dom.minidom
from datetime import datetime

import requests
import xmltodict

from usluga_payment.models import Operator

URL = "http://192.168.181.2/Operator.ashx"


def prepare_baip_account_data(transaction, operator, customer, action,**kwargs):
    return f"""<salesorder_request type="ns1:Msg_salesorder_soap_requestType">
  <general>
    <partner_transaction_id>{transaction.transaction_number}</partner_transaction_id>
    <kiosk_id>{operator.kiosk_id}</kiosk_id>
    <partner_contract_id>456</partner_contract_id>
    <host_ip>192.168.3.190</host_ip>
    <session_start>{datetime.now()}</session_start>
    <cashregister_id>{operator.cashregister_id}</cashregister_id>
    <receipt_id>{operator.receipt_id}</receipt_id>
    <partner_id>{operator.partner_id}</partner_id>
  </general>
  <products>
    <item>
      <partner_row_id>1</partner_row_id>
      <kiosk_productcode>2280007001455</kiosk_productcode>
      <partner_productcode>2280007001455</partner_productcode>
      <transaction_type>{action}</transaction_type>
      <quantity>1</quantity>
      <price>{transaction.amount}</price>
      <description>{{NL}}№ транзакции:{transaction.transaction_number}{{NL}}Абонент:{customer.name}{{NL}}</description >
      <partner_customer_id>1111</partner_customer_id>
    </item>
  </products>
</salesorder_request>""".encode(
        "utf-8"
    )


def send_baip_account_data(transaction, operator, action, customer):
    data = prepare_baip_account_data(transaction, operator, customer, action)
    headers = {"Content-Type": "application/xml"}

    try:
        response = requests.post(URL, data=data, headers=headers, timeout=3)
        response_content = xmltodict.parse(response.content)
    except Exception as exc:
        return False

    response = requests.post(URL, data=data, headers=headers)
    response_content = xmltodict.parse(response.content)

    return response_content


def cancel_baip_account_data(account_number, amount, action, name, **kwargs):
    operator = Operator.objects.latest()
    return f"""<salesorder_request type="ns1:Msg_salesorder_soap_requestType">
  <general>
    <partner_transaction_id></partner_transaction_id>
    <kiosk_id>{operator.kiosk_id}</kiosk_id>
    <partner_contract_id>264</partner_contract_id>
    <host_ip>192.168.3.224</host_ip>
    <session_start>{datetime.now()}</session_start>
    <cashregister_id>{operator.cashregister_id}</cashregister_id>
    <receipt_id>{operator.receipt_id}</receipt_id>
    <partner_id>{operator.partner_id}</partner_id>
  </general>
  <products>
    <item>
      <partner_row_id>1</partner_row_id>
      <kiosk_productcode>2280007001455</kiosk_productcode>
      <partner_productcode>2280007001455</partner_productcode>
      <transaction_type>RETURN</transaction_type>
      <quantity>1</quantity>
      <price>-{amount}</price>
      <description>Отмена платежа {{NL}} Транзакция {{NL}}: </description >
      <partner_customer_id>1111</partner_customer_id>
    </item>
  </products>
</salesorder_request>"""
