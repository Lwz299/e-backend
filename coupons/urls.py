from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_coupon, name='apply-coupon'),
    path('validate/', views.validate_coupon, name='validate-coupon'),
    path('create/', views.create_coupon, name='create-coupon'),
    path('list/', views.list_coupons, name='list-coupons'),
    path('<int:coupon_id>/disable/', views.disable_coupon, name='disable-coupon'),
]

