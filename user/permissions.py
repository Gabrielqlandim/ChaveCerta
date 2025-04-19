from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelfOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj == request.user

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.proprietario == request.user

class IsLocatarioOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.locatario == request.user

class IsEmailVerified(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active