from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view-wishlist'),
    path('add/', views.add_to_wishlist, name='add-to-wishlist'),
    path('<int:item_id>/remove/', views.remove_from_wishlist, name='remove-from-wishlist'),
]

