from django.http import Http404
from rest_framework import status,permissions
from receipt_generator_api.models import Receipt, User
from receipt_generator_api.serializers.generate_receipt_serializer import (
    GenerateReceiptSerializer,
)
from rest_framework import mixins,viewsets
from receipt_generator_api.lib.response import Response
from receipt_generator_api.data import DATA
from receipt_generator_api.utils import GenerateReceipt
import cloudinary.uploader


class GenerateReceiptViewset(mixins.CreateModelMixin,
                                mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Receipt.objects.all()
    serializer_class = GenerateReceiptSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, user_id):
        try:
            return User.objects.get(email=user_id)
        except Exception:
            raise Http404


    def create(self, request):
        data = request.data 
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            new_data=serializer.data
            x = GenerateReceipt([(new_data)])
            pdf = x.generate_pdf()
            f=[]
            for i in pdf:
                pdf_url = cloudinary.uploader.upload(i)
                f.append(pdf_url)
            pdf_list = [i["url"] for i in f]
            if not pdf_url:
                return Response(errors={"error":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data={"pdf_url":pdf_list},status = status.HTTP_201_CREATED)
            
        return Response(errors={'error':"please enter a valid number"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Receipt.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            dict(receipt=serializer.data, total=len(serializer.data)),
            status=status.HTTP_200_OK,
        )
