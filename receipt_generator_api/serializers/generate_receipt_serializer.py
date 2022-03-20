from rest_framework import serializers
from receipt_generator_api import models


class GenerateReceiptSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=265)
    mobile_number = serializers.CharField(max_length=265)
    address = serializers.CharField(max_length=265)
    class Meta:
        model = models.Receipt
        fields = ["name","mobile_number", "address", "total_amount_payable"]
        extra_kwargs = {
            "user": {"write_only": True},
        }
