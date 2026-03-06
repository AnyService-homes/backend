from rest_framework import generics, permissions
from accounts.permissions import IsVerifiedCompany
from .models import Company, Service, ServiceMan
from .serializers import CompanySerializer, ServiceSerializer, ServiceManSerializer


class CompanyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedCompany]

    def get_object(self):
        return self.request.user.company_profile


class CompanyServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedCompany]

    def get_queryset(self):
        return self.request.user.company_profile.services.all()

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company_profile)


class CompanyServiceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedCompany]

    def get_queryset(self):
        return self.request.user.company_profile.services.all()


class CompanyServiceManListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceManSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedCompany]

    def get_queryset(self):
        return self.request.user.company_profile.service_men.all()

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company_profile)


class CompanyServiceManUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceManSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifiedCompany]

    def get_queryset(self):
        return self.request.user.company_profile.service_men.all()