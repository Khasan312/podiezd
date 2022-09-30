from django.apps import AppConfig


class UslugaPaymentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usluga_payment"


    # def ready(self) -> None:
    #     # return super().ready()
    #     import usluga_payment.utils