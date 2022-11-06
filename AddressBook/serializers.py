from rest_framework import serializers
from .models import AddressB

class AddressBSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddressB
        fields="__all__"
        # fields = (
        #     'user_name',
        #     'Address_Line1',
        #     'Landmark',
        #     'Pincode',
        #     'State',
        #     'created',
        # )