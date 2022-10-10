import json
from rest_framework.response import Response
from rest_framework.views import APIView
from usluga_payment.payment import check_account, make_payment
from usluga_payment.serializers import MakePaymentSerializer
from usluga_payment.baip_request import send_baip_account_data
from usluga_payment.models import Transaction, Podiezd, BaipInfo
from rest_framework.generics import DestroyAPIView
from usluga_payment.cancel_baip_request import cancel_baip_account_data


class CheckAccount(APIView):
    def post(self, request, *args, **kwargs):
        account = json.loads(request.body)["account_number"]
        result = check_account(account)
    

        if result["success"] is False:
            return Response(result, status=404)
        name = result['message']
        baip_info = BaipInfo.objects.latest()

        transaction = Transaction.objects.create(
            transaction_number= account, name=name, baip_info=baip_info
        )

        
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
        transaction = Transaction.objects.filter(transaction_number=validated_data['account_number']).first()
        transaction.status = 'received'
        transaction.save()
        validated_data["action"] = "pay"
        validated_data['name'] = transaction.name
        send_baip_account_data(
            validated_data['account_number'],
            validated_data['amount'],
            validated_data['action'],
            validated_data['name'],

        )
        # print(validated_data)
        # print(transaction)

        # add the action field to the data to save action to database

        # save object to database
        serializer.save(**validated_data)

        return Response(result, status=200)

    
        
class TransactionCancel(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        

        serializer = MakePaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        info = Transaction.objects.get(random_number)

        info.status = 'cancelled'

        info.save()

        cancel_baip_account_data(account_number=Podiezd.random_number
                                )
        # serializer.save(**validated_data)

        return Response(status=200)
        