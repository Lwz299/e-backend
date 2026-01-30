from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create-order'),
    path('my-orders/', views.my_orders, name='my-orders'),
    path('<int:order_id>/', views.order_details, name='order-details'),
    path('all/', views.all_orders, name='all-orders'),
    path('<int:order_id>/status/', views.update_order_status, name='update-order-status'),
]

