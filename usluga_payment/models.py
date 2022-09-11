from django.db import models
import requests
import json

class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    action = models.CharField(max_length=50)



    # def get_info(self):
    #     r = requests.get('https://billing.crm.mycloud.kg/pay/main.php')
    #     ger_info = r.json()['message']
    #     for i in ger_info.values():
    #         print(i)
