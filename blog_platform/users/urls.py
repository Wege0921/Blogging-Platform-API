from django.urls import path
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView, 
    UserListCreateView, 
    UserDetailView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
