from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductListSerializer
from coupons.serializers import CouponSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    coupon = CouponSerializer(read_only=True)
    coupon_code = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'coupon', 'coupon_code', 'status', 'total_price', 'final_price', 'items', 'created_at')
        read_only_fields = ('user', 'status', 'total_price', 'final_price', 'created_at')

