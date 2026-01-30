from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ProductViewSet

# Use SimpleRouter instead of DefaultRouter to avoid automatic API root
router = SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls

