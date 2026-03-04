from django.urls import path
from .views import (
    CreateOrderView,
    CustomerOrdersView,
    ServiceManOrdersView,
    UpdateOrderStatusView,
    RateOrderView
)

urlpatterns = [
    path('create/', CreateOrderView.as_view()),
    path('customer/', CustomerOrdersView.as_view()),
    path('service-man/', ServiceManOrdersView.as_view()),
    path('<int:order_id>/status/', UpdateOrderStatusView.as_view()),
    path('<int:order_id>/rate/', RateOrderView.as_view()),
]