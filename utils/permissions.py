from rest_framework import permissions

class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.user_type == 'Instructor'
        
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user
    
class IsCourseOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.instructor == request.user




class IsRegistered(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
