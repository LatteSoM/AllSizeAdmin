from rest_framework.permissions import BasePermission

from api_app.models import Roles


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role_id == Roles.objects.get(name='admin'))


class IsDefaultUser(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return bool(request.user and request.user.role_id == Roles.objects.get(name='user'))


class Obshiy(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.role_id == Roles.objects.get(name='user')
                    or request.user.role_id == Roles.objects.get(name='admin')))



