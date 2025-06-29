# blog/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):


    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS болсо — уруксат беребиз
        if request.method in SAFE_METHODS:
            return True

        # PUT, PATCH, DELETE болсо — автор гана
        return obj.author == request.user
