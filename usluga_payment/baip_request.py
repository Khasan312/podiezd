from datetime import datetime

def test_check_account(account_number,amount, action):
    text = f"""<salesorder_request type="ns1:Msg_salesorder_soap_requestType">
  <general>
    <account_number>{account_number}</account_number>
    <refill_date_time>{datetime.now()}</refill_date_time>
    <amount>{amount}</amount>
    <action>{action}</action>
  </general>
  <products>
    <item>
      <partner_row_id>1</partner_row_id>
      <kiosk_productcode>2280007001431</kiosk_productcode>
      <partner_productcode>2280007001431</partner_productcode>
      <transaction_type>SALES</transaction_type>
      <quantity>1</quantity>
      <price>${price}</price>
      <description>ФИО:${json.payer_name}{NL}Лиц-й счет:${json.account}{NL}Номер транзакции:${json.txn_id}{NL}Тип оплаты: ${json.service}{NL}</description >
      <partner_customer_id>1111</partner_customer_id>
    </item>
  </products>
</salesorder_request>"""
    return text
