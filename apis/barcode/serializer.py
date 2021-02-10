from rest_framework import serializers

from apis.barcode.model import Barcode


class BarcodeSerializer(serializers.ModelSerializer):
    barcode_number = serializers.CharField(required=True, )

    class Meta:
        model = Barcode
        exclude = ('id', )


class BarcodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        exclude = ('id', )