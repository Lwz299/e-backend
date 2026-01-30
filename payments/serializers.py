from rest_framework import serializers
from .models import Payment
from orders.serializers import OrderSerializer
import uuid


class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id', read_only=True)
    order_total = serializers.DecimalField(source='order.final_price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'order_id', 'order_total', 'method', 'status', 'transaction_id', 'amount', 'paid_at')
        read_only_fields = ('transaction_id', 'paid_at')

