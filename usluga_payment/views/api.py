from ast import operator
import json

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from usluga_payment.baip_request import (
    cancel_baip_account_data,
    send_baip_account_data,
)
from usluga_payment.models import Customer, Operator, Podiezd, Transaction
from usluga_payment.payment import check_account, make_payment
from usluga_payment.serializers import (
    CustomerSerializer,
    MakePaymentSerializer,
    OperatorReadSerializer,
    OperatorSerializer,
    PodiezdSerializer,
    TransactionSerializer,
)
from rest_framework import status


class CheckAccount(APIView):
    def post(self, request, *args, **kwargs):
        account = json.loads(request.body)["account_number"]
        operator_id = json.loads(request.body)["operator_id"]

        customer = Customer.objects.filter(account_number=account)
        operator = Operator.objects.filter(operator_id=operator_id).first()

        if customer.exists():
            # create new transcation object
            transaction = Transaction.objects.create(
                customer=customer.first(), operator=operator
            )
            return Response(
                data={
                    "customer": CustomerSerializer(
                        instance=customer.first()
                    ).data,
                    "transaction": TransactionSerializer(
                        instance=transaction
                    ).data,
                },
                status=status.HTTP_200_OK,
            )

        result = check_account(account)

        if result["success"] is False:
            return Response(result, status=404)

        customer = Customer.objects.create(
            name=result["message"], account_number=account
        )

        # create new transcation object
        transaction = Transaction.objects.create(
            customer=customer, operator=operator
        )

        return Response(
            {
                "customer": CustomerSerializer(instance=customer).data,
                "transaction": TransactionSerializer(
                    instance=transaction
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class MakePayment(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        # validate request data
        serializer = MakePaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # get validated data
        validated_data = serializer.validated_data

        customer = Customer.objects.filter(
            account_number=validated_data["account_number"]
        )

        if not customer.exists():
            raise APIException("Customer not found", code=404)

        # make request payment
        result = make_payment(
            validated_data["account_number"], validated_data["amount"]
        )

        if result["success"] is False:
            raise APIException(result, code=404)

        transaction = Transaction.objects.filter(
            transaction_number=validated_data["transaction_num"]
        ).first()

        # update transaction status
        transaction.status = "received"
        transaction.amount = validated_data["amount"]
        transaction.save()

        if "operator_id" in data:
            operator = Operator.objects.filter(operator_id=data["operator_id"])

            if operator.exists():
                operator = operator.first()
            else:
                operator = Operator.objects.latest()
        else:
            operator = Operator.objects.latest()

        # send into payment information
        payment = send_baip_account_data(
            transaction=transaction,
            operator=operator,
            action="pay",
            customer=customer.first(),
        )

        # if not payment:
        #     raise APIException(
        #         {"message": "Payment was not complete", "status": False},
        #         code=status.HTTP_400_BAD_REQUEST,
        #     )

        return Response(result, status=200)


class TransactionCancel(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        print('---------------------------')

        serializer = TransactionSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        customer = Customer.objects.filter(
            account_number=validated_data["account_number"]
        )
        if not customer.exists():
            raise APIException("Customer not found", code=404)


        transaction = Transaction.objects.filter(transaction_number=validated_data['transaction_num']).first()

        transaction.status = "cancelled"
        transaction.amount = validated_data["amount"]
        transaction.save()

        cancel_baip_account_data(account_number=validated_data['account_number'])

        return Response(status=200)


class OperatorInfoView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = OperatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        operator = Operator.objects.filter(**serializer.validated_data)

        if not operator.exists():
            serializer.save()
            return Response(
                data=OperatorReadSerializer(instance=serializer.instance).data,
                status=200,
            )

        return Response(
            data=OperatorReadSerializer(instance=operator.first()).data,
            status=200,
        )
