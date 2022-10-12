from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from usluga_payment.models import Podiezd


class MakePaymentSerializer(ModelSerializer):
    class Meta:
        model = Podiezd
        fields = ["account_number", "amount"]

    def validate(self, attrs):
        if attrs["amount"] < 0:
            raise serializers.ValidationError("amount can not be negative")

        return attrs


class TransactionCancelSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()


class PodiezdSerializer(ModelSerializer):
    class Meta:
        model = Podiezd
        fields = "__all__"
