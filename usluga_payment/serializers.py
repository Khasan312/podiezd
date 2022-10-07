from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Podiezd


class MakePaymentSerializer(ModelSerializer):
    class Meta:
        model = Podiezd
        fields = ["account_number", "amount"]
        # fields = '__all__'

    def validate(self, attrs):
        if attrs["amount"] < 0:
            raise serializers.ValidationError("amount can not be negative")

        return attrs



class TransactionCancelSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()