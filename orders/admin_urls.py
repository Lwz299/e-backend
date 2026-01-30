from django.urls import path
from . import admin_views

urlpatterns = [
    path('dashboard/stats/', admin_views.dashboard_stats, name='dashboard-stats'),
    path('dashboard/sales-report/', admin_views.sales_report, name='sales-report'),
    path('dashboard/stock-report/', admin_views.product_stock_report, name='stock-report'),
]

