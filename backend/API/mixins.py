
from rest_framework import permissions
from .permissions import IsEditorPermissions

class EditorPermsMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsEditorPermissions
    ]

class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if user.is_staff:
            return qs
        return qs.filter(**lookup_data)