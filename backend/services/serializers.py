from rest_framework import serializers
from .models import Category, Company, Service, ServiceMan


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'created_at']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'logo', 'description',
            'phone', 'email', 'address', 'website',
            'rating', 'created_at'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'description', 'price',
            'category', 'company', 'created_at'
        ]


class ServiceManSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = ServiceMan
        fields = ['id', 'full_name', 'phone', 'is_available', 'company']