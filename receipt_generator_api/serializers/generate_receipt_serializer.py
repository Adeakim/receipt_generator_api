from rest_framework import serializers
from receipt_generator_api import models


class GenerateReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Receipt
        fields = ['user', 'email', 'name','address', 'total_amount_payable']
        read_only_fields = [ 
            "name",
            "address",
            'email',
        ]
        extra_kwargs = {
            'user': {'write_only': True},
        }