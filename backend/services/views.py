from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Company, Service, ServiceMan
from .serializers import (
    CategorySerializer, CompanySerializer,
    ServiceSerializer, ServiceManSerializer
)
from .filters import ServiceFilter


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        # Only verified companies appear in the app
        return Company.objects.filter(is_verified=True).order_by('name')


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        # Only services from verified companies
        return Service.objects.filter(company__is_verified=True).order_by('name')


class ServicesByCategoryView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        # Only services from verified companies in this category
        return Service.objects.filter(
            category_id=self.kwargs['category_id'],
            company__is_verified=True
        ).order_by('name')


class ServicesByCompanyView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        # Only show services if the company is verified
        return Service.objects.filter(
            company_id=self.kwargs['company_id'],
            company__is_verified=True
        ).order_by('name')


class ServiceMenByCompanyView(generics.ListAPIView):
    serializer_class = ServiceManSerializer

    def get_queryset(self):
        # Only service men from verified companies
        return ServiceMan.objects.filter(
            company_id=self.kwargs['company_id'],
            company__is_verified=True
        )


class SearchServicesView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        # Search only inside verified companies
        return Service.objects.filter(
            name__icontains=q,
            company__is_verified=True
        ).order_by('name')


class FilterServicesView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_queryset(self):
        # Filter only services from verified companies
        return Service.objects.filter(company__is_verified=True).order_by('name')