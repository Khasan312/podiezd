from random import randint

from django.db import models
from django.utils import timezone

from .utils import create_new_ref_number

# from django.dispatch import receiver
LENGTH = 20


def random_string():
    return randint(10000, 99999)


class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    action = models.CharField(max_length=50)
    transaction_id = models.CharField(
        max_length=20,
        blank=True,
        editable=False,
        unique=True,
        default=create_new_ref_number,
    )
    name = models.CharField(max_length=164)

    class Meta:
        get_latest_by = ["refill_date_time"]

    def __str__(self) -> str:
        return f"action -> {self.action}"


class BaipInfo(models.Model):
    cashregister_id = models.IntegerField()
    kiosk_id = models.IntegerField()
    receipt_id = models.IntegerField()
    partner_id = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        get_latest_by = ["created"]

    def __str__(self):
        return str(self.cashregister_id)


class Transaction(models.Model):
    class TransactionStatus(models.TextChoices):
        RECIEVED = ("received", "RECEIVED")
        CANCELLED = ("cancelled", "CANCELLED")
        WAITING = ("waiting", "WAITING")

    transaction_number = models.IntegerField()
    name = models.CharField(max_length=128)
    baip_info = models.ForeignKey(
        BaipInfo, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(
        max_length=32,
        choices=TransactionStatus.choices,
        default=TransactionStatus.WAITING,
    )

    def __str__(self):
        return str(self.transaction_number)
