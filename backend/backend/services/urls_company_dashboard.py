from django.urls import path
from .views_company_dashboard import (
    CompanyProfileView,
    CompanyServiceListCreateView,
    CompanyServiceUpdateDeleteView,
    CompanyServiceManListCreateView,
    CompanyServiceManUpdateDeleteView
)

urlpatterns = [
    path('profile/', CompanyProfileView.as_view()),

    path('services/', CompanyServiceListCreateView.as_view()),
    path('services/<int:pk>/', CompanyServiceUpdateDeleteView.as_view()),

    path('service-men/', CompanyServiceManListCreateView.as_view()),
    path('service-men/<int:pk>/', CompanyServiceManUpdateDeleteView.as_view()),
]