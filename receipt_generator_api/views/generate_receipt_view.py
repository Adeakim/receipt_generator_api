from rest_framework.viewsets import ModelViewSet
from rest_framework import status,permissions
# from rest_framework.response import Response
from receipt_generator_api.models import Receipt, User
from receipt_generator_api.serializers.generate_receipt_serializer import (
    GenerateReceiptSerializer,
)
from receipt_generator_api.lib.response import Response
from receipt_generator_api.data import DATA
from receipt_generator_api.utils import GenerateReceipt
import cloudinary.uploader


class GenerateReceiptViewset(ModelViewSet):
    queryset = Receipt
    serializer_class = GenerateReceiptSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        data = request.data 
        user_id = data.get("user")
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = User.objects.get(email=user_id)
            serializer.save(email=user.email,name=user.name,address=user.address, mobile_number=user.mobile_number)
            new_data=serializer.data
            x = GenerateReceipt([(new_data)])
            pdf = x.generate_pdf(user.name)
            pdf_url = cloudinary.uploader.upload(pdf)
            
            return Response(data={"data":serializer.data,"pdf_url":pdf_url['url']},status = status.HTTP_201_CREATED)
        return Response(errors={'error':"please enter a valid number"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Receipt.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            dict(receipt=serializer.data, total=len(serializer.data)),
            status=status.HTTP_200_OK,
        )
