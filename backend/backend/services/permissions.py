from rest_framework.permissions import BasePermission

class IsCompanyAdmin(BasePermission):
    """
    Allows access only to users with role = company_admin.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            getattr(request.user, "role", None) == "company_admin"
        )