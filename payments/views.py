from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Payment
from orders.models import Order
from .serializers import PaymentSerializer
import uuid


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def virtual_payment(request):
    order_id = request.data.get('order_id')
    method = request.data.get('method', 'virtual_card')
    
    if not order_id:
        return Response(
            {'error': 'order_id is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Check if payment already exists
    if Payment.objects.filter(order=order).exists():
        return Response(
            {'error': 'Payment already exists for this order.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Generate transaction ID
    transaction_id = f"TXN-{timezone.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
    
    # Create virtual payment (always success for virtual payment)
    payment = Payment.objects.create(
        order=order,
        method=method,
        status='success',
        transaction_id=transaction_id,
        amount=order.final_price
    )
    
    # Update order status to paid
    order.status = 'paid'
    order.save()
    
    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_status(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    try:
        payment = Payment.objects.get(order=order)
    except Payment.DoesNotExist:
        return Response(
            {'error': 'Payment not found for this order.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = PaymentSerializer(payment)
    return Response(serializer.data)
