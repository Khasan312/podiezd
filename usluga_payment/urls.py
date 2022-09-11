from django.urls import path

from .views.api import CheckAccount, MakePayment
from .views.main import index

urlpatterns = [
    path("", index, name="index"),
    path("api/check-account", CheckAccount.as_view(), name="check_account_api"),
    path("api/make-payment", MakePayment.as_view(), name="make_account_api"),
]
