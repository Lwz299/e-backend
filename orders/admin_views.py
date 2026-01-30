from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from orders.models import Order, OrderItem
from products.models import Product
from payments.models import Payment
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([IsAdminUser])
def dashboard_stats(request):
    # Total stats
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Payment.objects.filter(status='success').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    # Recent orders (last 7 days)
    seven_days_ago = timezone.now() - timedelta(days=7)
    recent_orders = Order.objects.filter(created_at__gte=seven_days_ago).count()
    
    # Pending orders
    pending_orders = Order.objects.filter(status='pending').count()
    
    # Low stock products
    low_stock_products = Product.objects.filter(stock__lt=10).count()
    
    return Response({
        'total_users': total_users,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': float(total_revenue),
        'recent_orders': recent_orders,
        'pending_orders': pending_orders,
        'low_stock_products': low_stock_products,
    })


@api_view(['GET'])
@permission_classes([IsAdminUser])
def sales_report(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    
    payments = Payment.objects.filter(status='success')
    
    if start_date:
        payments = payments.filter(paid_at__gte=start_date)
    if end_date:
        payments = payments.filter(paid_at__lte=end_date)
    
    total_sales = payments.aggregate(total=Sum('amount'))['total'] or 0
    total_orders = payments.count()
    
    # Daily sales breakdown
    daily_sales = payments.values('paid_at__date').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('paid_at__date')
    
    return Response({
        'total_sales': float(total_sales),
        'total_orders': total_orders,
        'daily_sales': list(daily_sales),
    })


@api_view(['GET'])
@permission_classes([IsAdminUser])
def product_stock_report(request):
    products = Product.objects.all().order_by('stock')
    
    low_stock = products.filter(stock__lt=10)
    out_of_stock = products.filter(stock=0)
    
    report = {
        'total_products': products.count(),
        'low_stock_count': low_stock.count(),
        'out_of_stock_count': out_of_stock.count(),
        'low_stock_products': [
            {
                'id': p.id,
                'name': p.name,
                'stock': p.stock,
                'price': float(p.price)
            }
            for p in low_stock
        ],
        'out_of_stock_products': [
            {
                'id': p.id,
                'name': p.name,
                'stock': p.stock,
                'price': float(p.price)
            }
            for p in out_of_stock
        ],
    }
    
    return Response(report)

