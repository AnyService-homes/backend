from django.contrib import admin
from .models import Company, Category, Service, ServiceMan

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'category', 'price')
    list_filter = ('company', 'category')
    search_fields = ('name', 'company__name', 'category__name')
    ordering = ('name',)


@admin.register(ServiceMan)
class ServiceManAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'phone')
    list_filter = ('company',)
    search_fields = ('full_name', 'company__name')
    ordering = ('full_name',)