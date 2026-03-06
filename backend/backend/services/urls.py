from django.urls import path
from .views import (
    CategoryListView,
    CompanyListView,
    FilterServicesView,
    ServiceListView,
    ServicesByCategoryView,
    ServicesByCompanyView,
    ServiceMenByCompanyView,
    SearchServicesView,
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),

    # Companies
    path('companies/', CompanyListView.as_view(), name='company-list'),

    # All services
    path('list/', ServiceListView.as_view(), name='service-list'),

    # Services by category
    path('category/<int:category_id>/', ServicesByCategoryView.as_view(), name='services-by-category'),

    # Services by company
    path('company/<int:company_id>/', ServicesByCompanyView.as_view(), name='services-by-company'),

    # Service men by company
    path('company/<int:company_id>/service-men/', ServiceMenByCompanyView.as_view(), name='service-men-by-company'),

    # Search
    path('search/', SearchServicesView.as_view(), name='service-search'),

    # Filter services
    path('filter/', FilterServicesView.as_view()),
]