from rest_framework import permissions


class IsAdminUserCustom(permissions.BasePermission):
    """
    Faqat is_admin=True userlar uchun.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin)
