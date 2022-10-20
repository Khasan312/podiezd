from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from usluga_payment.models import Customer, Operator, Podiezd, Transaction


class MakePaymentSerializer(serializers.Serializer):
    account_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=9, decimal_places=2)
    transaction_num = serializers.IntegerField()

    def validate(self, attrs):
        if attrs["amount"] < 0:
            raise serializers.ValidationError("amount can not be negative")

        return attrs


class TransactionCancelSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    operator_id = serializers.CharField()


class PodiezdSerializer(ModelSerializer):
    class Meta:
        model = Podiezd
        fields = "__all__"


class OperatorSerializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = ["cashregister_id", "kiosk_id", "receipt_id", "partner_id"]


class OperatorReadSerializer(OperatorSerializer):
    class Meta(OperatorSerializer.Meta):
        fields = OperatorSerializer.Meta.fields + ["operator_id"]


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    operator = OperatorReadSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
