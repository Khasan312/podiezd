from django.db import models
import requests
import json


class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    action = models.CharField(max_length=50)



    def __str__(self) -> str:
        return f' account_num -> {str(self.account_number)} and action -> {self.action}'