from rest_framework.permissions import BasePermission

class IsVerifiedCompany(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.role != "company":
            return False

        if not hasattr(user, "company_profile"):
            return False

        return user.company_profile.is_verified