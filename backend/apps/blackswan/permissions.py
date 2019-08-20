from rest_framework import permissions


class IsOwnerOrPublic(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return not obj.private or request.user in obj.user_set.all()
