from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.product_reviews, name='product-reviews'),
    path('add/', views.add_review, name='add-review'),
    path('<int:review_id>/', views.update_review, name='update-review'),
    path('<int:review_id>/delete/', views.delete_review, name='delete-review'),
]

