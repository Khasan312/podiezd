from email.policy import default
from random import randint
from uuid import uuid4

from django.db import models
from django.utils import timezone

from .utils import create_new_ref_number

# from django.dispatch import receiver
LENGTH = 20


def random_string():
    return randint(10000, 99999999)


class Operator(models.Model):
    cashregister_id = models.IntegerField()
    kiosk_id = models.IntegerField()
    receipt_id = models.IntegerField()
    partner_id = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    operator_id = models.CharField(max_length=128, default=uuid4)

    class Meta:
        get_latest_by = ["created"]

    def __str__(self):
        return str(self.operator_id)


class Customer(models.Model):
    account_number = models.IntegerField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class TransactionStatus(models.TextChoices):
        RECIEVED = ("received", "RECEIVED")
        CANCELLED = ("cancelled", "CANCELLED")
        WAITING = ("waiting", "WAITING")

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True
    )
    transaction_number = models.CharField(
        max_length=128, default=random_string
    )
    operator = models.ForeignKey(
        Operator, on_delete=models.SET_NULL, null=True
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0
    )
    status = models.CharField(
        max_length=32,
        choices=TransactionStatus.choices,
        default=TransactionStatus.WAITING,
    )

    def __str__(self):
        return str(self.transaction_number)


class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"action -> {self.action}"
