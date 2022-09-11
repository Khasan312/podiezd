import json

from rest_framework.response import Response
from rest_framework.views import APIView
from usluga_payment.payment import check_account, make_payment
from usluga_payment.serializers import MakePaymentSerializer


class CheckAccount(APIView):
    def post(self, request, *args, **kwargs):
        account = json.loads(request.body)["account_number"]
        result = check_account(account)

        if result["success"] is False:
            return Response(result, status=404)

        return Response(result, status=200)


class MakePayment(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        # validate request data
        serializer = MakePaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        result = make_payment(
            validated_data["account_number"], validated_data["amount"]
        )

        if result["success"] is False:
            return Response(result, status=404)

        # add the action field to the data to save action to database
        validated_data["action"] = "pay"

        # save object to database
        serializer.save(**validated_data)

        return Response(result, status=200)
