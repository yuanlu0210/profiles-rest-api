from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id


class UpdateOwnStatus(permissions.BasePermission):
    """Alow user to update their own status"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.user_profile.id