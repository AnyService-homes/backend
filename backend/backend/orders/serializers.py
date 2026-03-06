from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order
from services.serializers import ServiceSerializer

class UserMiniSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'phone']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

    def get_phone(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.phone
        return None


class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)
    booking_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'service', 'service_id',
            'booking_time', 'status', 'created_at'
        ]