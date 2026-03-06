from django_filters import rest_framework as filters
from .models import Service

class ServiceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    company = filters.NumberFilter(field_name="company_id")
    category = filters.NumberFilter(field_name="category_id")

    class Meta:
        model = Service
        fields = ['company', 'category', 'min_price', 'max_price']