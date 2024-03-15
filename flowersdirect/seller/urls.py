from django.urls import path
from .views import SellerDashboard, OrderDetails

urlpatterns = [
    path('dashboard/', SellerDashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
]