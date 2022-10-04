import requests
from datetime import datetime
import xmltodict


URL = 'http://192.168.181.2/Operator.ashx'

def prepare_baip_account_data(account_number,amount, action):
     return  f"""<?xml version='1.0' encoding='utf-8'?>
<salesorder_request type="ns1:Msg_salesorder_soap_requestType">
  <general>
    <partner_transaction_id>1</partner_transaction_id>
    <kiosk_id>724300</kiosk_id>
    <partner_contract_id>456</partner_contract_id>
    <host_ip>192.168.3.190</host_ip>
    <session_start>{datetime.now()}</session_start>
    <cashregister_id>{account_number}</cashregister_id>
    <receipt_id>420</receipt_id>
    <partner_id>513744</partner_id>
  </general>
  <products>
    <item>
      <partner_row_id>1</partner_row_id>
      <kiosk_productcode>2280007001455</kiosk_productcode>
      <partner_productcode>2280007001455</partner_productcode>
      <transaction_type>{action}</transaction_type>
      <quantity>1</quantity>
      <price>{amount}</price>
      <description>Улан Джумашев</description >
      <partner_customer_id>1111</partner_customer_id>
    </item>
  </products>
</salesorder_request>""".encode("utf-8")



def send_baip_account_data(account_number,amount, action):
  data = prepare_baip_account_data(account_number, amount, action)

  response = requests.post(URL, data=data)
  print('---------------------')
  print(response.content)
  response_content = xmltodict.parse(response.content)

  return response_content