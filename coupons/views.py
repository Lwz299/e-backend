from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Coupon
from .serializers import CouponSerializer, ApplyCouponSerializer, ValidateCouponSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_coupon(request):
    serializer = ApplyCouponSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    code = serializer.validated_data['code']
    
    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        return Response(
            {'error': 'Invalid coupon code.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    now = timezone.now()
    
    if not coupon.is_active:
        return Response(
            {'error': 'Coupon is not active.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if coupon.valid_from > now or coupon.valid_to < now:
        return Response(
            {'error': 'Coupon is expired or not yet valid.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if coupon.used_count >= coupon.max_usage:
        return Response(
            {'error': 'Coupon usage limit reached.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    return Response({
        'message': 'Coupon is valid.',
        'coupon': CouponSerializer(coupon).data,
        'discount_percentage': coupon.discount_percentage
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def validate_coupon(request):
    serializer = ValidateCouponSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    code = serializer.validated_data['code']
    
    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        return Response(
            {'valid': False, 'message': 'Invalid coupon code.'},
            status=status.HTTP_200_OK
        )
    
    now = timezone.now()
    is_valid = (
        coupon.is_active and
        coupon.valid_from <= now <= coupon.valid_to and
        coupon.used_count < coupon.max_usage
    )
    
    return Response({
        'valid': is_valid,
        'coupon': CouponSerializer(coupon).data if is_valid else None,
        'message': 'Coupon is valid.' if is_valid else 'Coupon is invalid or expired.'
    })


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_coupon(request):
    serializer = CouponSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_coupons(request):
    coupons = Coupon.objects.all()
    serializer = CouponSerializer(coupons, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def disable_coupon(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    coupon.is_active = False
    coupon.save()
    return Response({
        'message': 'Coupon disabled successfully.',
        'coupon': CouponSerializer(coupon).data
    })
