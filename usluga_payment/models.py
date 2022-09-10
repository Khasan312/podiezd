from django.db import models

class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    action = models.CharField(max_length=50)
