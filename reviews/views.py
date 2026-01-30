from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Review
from products.models import Product
from .serializers import ReviewSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def product_reviews(request, product_id):
    reviews = Review.objects.filter(product_id=product_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request):
    product_id = request.data.get('product_id')
    
    if not product_id:
        return Response(
            {'error': 'product_id is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    review, created = Review.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={
            'rating': request.data.get('rating'),
            'comment': request.data.get('comment', '')
        }
    )

    if not created:
        return Response(
            {'error': 'You have already reviewed this product.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return Response({'message': 'Review deleted.'}, status=status.HTTP_200_OK)
