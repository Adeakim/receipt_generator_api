from rest_framework import serializers
from receipt_generator_api import models


class GenerateReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receipt
        fields = ["user", "name","mobile_number", "address", "total_amount_payable"]
        read_only_fields = [
            "name",
            "address",
            "mobile_number"
        ]
        extra_kwargs = {
            "user": {"write_only": True},
        }
