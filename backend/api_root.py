from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    API Root - Lists all available endpoints
    """
    base_url = request.build_absolute_uri('/').rstrip('/')
    
    return Response({
        'message': 'Welcome to E-commerce API',
        'version': '1.0',
        'endpoints': {
            'auth': {
                'register': f'{base_url}/api/auth/register/',
                'login': f'{base_url}/api/auth/login/',
                'refresh': f'{base_url}/api/auth/refresh/',
                'profile': f'{base_url}/api/auth/profile/',
            },
            'products': {
                'list': f'{base_url}/api/products/',
                'categories': f'{base_url}/api/categories/',
            },
            'cart': {
                'view': f'{base_url}/api/cart/',
                'add': f'{base_url}/api/cart/add/',
            },
            'wishlist': {
                'view': f'{base_url}/api/wishlist/',
                'add': f'{base_url}/api/wishlist/add/',
            },
            'reviews': {
                'add': f'{base_url}/api/reviews/add/',
                'product_reviews': f'{base_url}/api/reviews/products/<product_id>/',
            },
            'coupons': {
                'validate': f'{base_url}/api/coupons/validate/',
                'apply': f'{base_url}/api/coupons/apply/',
            },
            'orders': {
                'create': f'{base_url}/api/orders/create/',
                'my_orders': f'{base_url}/api/orders/my-orders/',
            },
            'payments': {
                'pay': f'{base_url}/api/payments/pay/',
                'status': f'{base_url}/api/payments/status/<order_id>/',
            },
            'admin': {
                'dashboard': f'{base_url}/api/admin/dashboard/stats/',
                'sales_report': f'{base_url}/api/admin/dashboard/sales-report/',
                'stock_report': f'{base_url}/api/admin/dashboard/stock-report/',
            },
        },
        'authentication': {
            'type': 'JWT Bearer Token',
            'header': 'Authorization: Bearer <token>',
            'get_token': f'{base_url}/api/auth/login/',
        },
        'documentation': 'See API_DOCUMENTATION.md for full API documentation',
    })

