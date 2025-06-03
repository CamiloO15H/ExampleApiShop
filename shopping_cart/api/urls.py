from django.urls import path
from .views import CartItemviews

urlpatterns = [
    path('cart-items/', CartItemviews.as_view()),  # Endpoint for cart items
    path('cart-items/<int:pk>/', CartItemviews.as_view()),  # Endpoint for a specific cart item
]