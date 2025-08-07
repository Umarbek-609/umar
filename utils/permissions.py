from rest_framework import permissions
from user.models import CustomUser
# class IsOwnerOrReadOnly(permissions.BasePermission):

class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.user_type == 'Instructor'
        
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user
    
class IsCourseOwnerOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.instructor == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.instructor == request.user




class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user: CustomUser = request.user
        return user.user_type == CustomUser.UserTypeEnum.STUDENT
    
class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user: CustomUser = request.user
        return user.user_type == CustomUser.UserTypeEnum.Instructor