from django.urls import path

from .views.api import (
    CheckAccount,
    MakePayment,
    TransactionCancel,
    OperatorInfoView,
    
)
from .views.main import index

urlpatterns = [
    path("", index, name="index"),
    # Check account
    path(
        "api/check-account", CheckAccount.as_view(), name="check_account_api"
    ),
    # Payment
    path("api/make-payment", MakePayment.as_view(), name="make_account_api"),
    # Cancel Payment

    path(
        "api/cancel-payment",
        TransactionCancel.as_view(),
        name="cancel_account_api",
    ),
    # Operator Info
    path(
        "api/operator-info",
        OperatorInfoView.as_view(),
        name="operator_info_api",
    ),
    
]
