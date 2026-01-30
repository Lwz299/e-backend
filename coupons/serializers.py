from rest_framework import serializers
from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class ApplyCouponSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)


class ValidateCouponSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)

