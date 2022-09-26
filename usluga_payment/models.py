from django.db import models
from .utils import unique_number_generator
from django.db.models.signals import pre_save


class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    action = models.CharField(max_length=50)
    random_number = models.CharField(max_length=20, null=True, blank=True, unique=True)



    def __str__(self) -> str:
        return f' account_num -> {str(self.account_number)} and action -> {self.action}'



def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instnace.random_number:
        instance.random_number = unique_number_generator(instance)
pre_save.connect(pre_save_create_order_id, sender=Podiezd)