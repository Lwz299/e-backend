from rest_framework import serializers
from .models import Review
from products.serializers import ProductListSerializer
from accounts.serializers import UserProfileSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    product = ProductListSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user_username', 'product', 'product_id', 'rating', 'comment', 'created_at')
        read_only_fields = ('user_username', 'created_at')

