from rest_framework import viewsets

from apis.models import Barcode
from apis.barcode.serializer import BarcodeSerializer, BarcodeListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer

    def get_queryset(self):
        queryset = Barcode.objects.filter(user_id=self.request.user.id)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        serializer = BarcodeListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)