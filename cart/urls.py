from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view-cart'),
    path('add/', views.add_to_cart, name='add-to-cart'),
    path('items/<int:item_id>/', views.update_quantity, name='update-quantity'),
    path('items/<int:item_id>/remove/', views.remove_item, name='remove-item'),
    path('clear/', views.clear_cart, name='clear-cart'),
]

