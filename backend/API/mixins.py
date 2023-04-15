
from rest_framework import permissions
from .permissions import IsEditorPermissions

class EditorPermsMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsEditorPermissions
    ]