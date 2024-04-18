from rest_framework.permissions import BasePermission
from users.models import Company


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Company.objects.filter(user=request.user).exists()
        return False
