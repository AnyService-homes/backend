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
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer


class ServicesByCategoryView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(category_id=self.kwargs['category_id']).order_by('name')


class ServicesByCompanyView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(company_id=self.kwargs['company_id']).order_by('name')


class ServiceMenByCompanyView(generics.ListAPIView):
    serializer_class = ServiceManSerializer

    def get_queryset(self):
        return ServiceMan.objects.filter(company_id=self.kwargs['company_id'])


class SearchServicesView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        return Service.objects.filter(name__icontains=q).order_by('name')


class FilterServicesView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter