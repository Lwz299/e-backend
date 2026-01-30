from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.virtual_payment, name='virtual-payment'),
    path('status/<int:order_id>/', views.payment_status, name='payment-status'),
]

