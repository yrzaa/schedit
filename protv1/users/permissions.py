from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''
    
    def has_object_permission(self, request, view, obj):
        #allowing GET method on all users
        if request.method in permissions.SAFE_METHODS:
            return True

        #checking if user is editing their own profile
        return obj.id == request.user.id