from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('refresh/', views.refresh_token_view, name='refresh-token'),
    path('profile/', views.my_profile_view, name='my-profile'),
    path('users/', views.UserListView.as_view(), name='list-users'),
    path('users/<int:user_id>/block/', views.block_unblock_user, name='block-user'),
]

