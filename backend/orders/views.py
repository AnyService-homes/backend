from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer


# 1) Create Order
class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


# 2) List Customer Orders
class CustomerOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


# 3) List Service Man Orders
class ServiceManOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(service_man=self.request.user).order_by('-created_at')


# 4) Update Order Status
class UpdateOrderStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        new_status = request.data.get("status")

        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=400)

        order.status = new_status
        order.save()

        return Response({"message": "Status updated", "order": OrderSerializer(order).data})


# 5) Add Rating + Feedback
class RateOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        order.rating = request.data.get("rating")
        order.feedback = request.data.get("feedback")
        order.save()

        return Response({"message": "Rating submitted", "order": OrderSerializer(order).data})
