from django.urls import path
from .views import TransportOrderListCreateView, TransportOrderDetailView

urlpatterns = [
    path('orders/', TransportOrderListCreateView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', TransportOrderDetailView.as_view(), name='orders-detail'),
]
