from datetime import datetime

from usluga_payment.models import BaipInfo


def cancel_baip_account_data(account_number, amount, action, name, **kwargs):
    baip_info = BaipInfo.objects.latest()
    return f"""<salesorder_request type="ns1:Msg_salesorder_soap_requestType">
  <general>
    <partner_transaction_id></partner_transaction_id>
    <kiosk_id>{baip_info.kiosk_id}</kiosk_id>
    <partner_contract_id>264</partner_contract_id>
    <host_ip>192.168.3.224</host_ip>
    <session_start>{datetime.now()}</session_start>
    <cashregister_id>{baip_info.cashregister_id}</cashregister_id>
    <receipt_id>{baip_info.receipt_id}</receipt_id>
    <partner_id>{baip_info.partner_id}</partner_id>
  </general>
  <products>
    <item>
      <partner_row_id>1</partner_row_id>
      <kiosk_productcode>2280007001455</kiosk_productcode>
      <partner_productcode>2280007001455</partner_productcode>
      <transaction_type>RETURN</transaction_type>
      <quantity>1</quantity>
      <price>-{amount}</price>
      <description>Отмена платежа{NL}Транзакция:{NL}</description >
      <partner_customer_id>1111</partner_customer_id>
    </item>
  </products>
</salesorder_request>"""
