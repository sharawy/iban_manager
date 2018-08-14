class ExtraObjectLevelPermission(object):
    permission_class = None

    def _valid_to_apply(self, request, obj, method_name):
        return not request.user.is_superuser and obj and self.permission_class and hasattr(self.permission_class,
                                                                                           method_name)

    def has_change_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj)
        if self._valid_to_apply(request, obj, 'has_change_permission'):
            return self.permission_class.has_change_permission(request, obj) and result
        return result

    def has_delete_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj)
        if self._valid_to_apply(request, obj, 'has_delete_permission'):
            return self.permission_class.has_delete_permission(request, obj) and result
        return result

    def has_add_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj)
        if self._valid_to_apply(request, obj, 'has_add_permission'):
            return self.permission_class.has_add_permission(request, obj) and result
        return result