from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsStudentPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            request.user.is_student
        except Exception:
            raise PermissionDenied
        return bool(request.user and request.user.is_student)


class IsElderPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            request.user.is_elder
        except Exception:
            raise PermissionDenied
        return bool(request.user and request.user.is_elder)
