from django.db import models
from .utils import create_new_ref_number 
# from django.dispatch import receiver
LENGTH = 20


def random_string():
    return (random.randint(10000, 99999))

class Podiezd(models.Model):
    account_number = models.IntegerField()
    refill_date_time = models.DateTimeField(
        auto_now_add=True
        )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2
        )
    action = models.CharField(
        max_length=50
        )
    random_number = models.CharField(
            max_length = 20,
            blank=True,
            editable=False,
            unique=True,
            default=create_new_ref_number
        )




    def __str__(self) -> str:
        return f' random_number -> {str(self.random_number)} and action -> {self.action}'

# @receiver(pre_save, sender=Podiezd)
# def pre_save_create_txn_id(sender, instance, *args, **kwargs):
#     if not instance.random_number:
#         instance.random_number = unique_txn_id_order(instance)

        
        


# def pre_save_create_order_id(sender, instance, *args, **kwargs):
#     if not instnace.random_number:
#         instance.random_number = unique_number_generator(instance)
#     return instance.random_number