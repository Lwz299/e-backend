from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from decimal import Decimal
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from coupons.models import Coupon
from .serializers import OrderSerializer, OrderItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    cart = Cart.objects.filter(user=request.user).first()
    
    if not cart or not cart.items.exists():
        return Response(
            {'error': 'Cart is empty.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    
    # Apply coupon if provided
    coupon_code = request.data.get('coupon_code', '')
    coupon = None
    discount_percentage = 0
    
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code)
            now = timezone.now()
            
            if (coupon.is_active and 
                coupon.valid_from <= now <= coupon.valid_to and 
                coupon.used_count < coupon.max_usage):
                discount_percentage = coupon.discount_percentage
                coupon.used_count += 1
                coupon.save()
            else:
                coupon = None
        except Coupon.DoesNotExist:
            pass
    
    # Calculate final price
    discount_amount = total_price * Decimal(discount_percentage) / 100
    final_price = total_price - discount_amount
    
    # Create order
    order = Order.objects.create(
        user=request.user,
        coupon=coupon,
        total_price=total_price,
        final_price=final_price,
        status='pending'
    )
    
    # Create order items
    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.product.price
        )
    
    # Clear cart
    cart.items.all().delete()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    new_status = request.data.get('status')
    
    if new_status not in dict(Order.STATUS_CHOICES):
        return Response(
            {'error': 'Invalid status.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    order.status = new_status
    order.save()
    
    serializer = OrderSerializer(order)
    return Response(serializer.data)
