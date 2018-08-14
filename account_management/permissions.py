class AllowOnlyCreatorToChangeDeleteUser(object):

    @staticmethod
    def has_change_permission(request, obj=None):
        return request.user == obj.created_by

    @staticmethod
    def has_delete_permission(request, obj=None):
        return request.user == obj.created_by

    @staticmethod
    def has_add_permission(request, obj=None):
        return request.user == obj.created_by


class AllowOnlyCreatorIBAN(object):

    @staticmethod
    def has_change_permission(request, obj=None):
        return request.user == obj.owner.created_by

    @staticmethod
    def has_delete_permission(request, obj=None):
        return request.user == obj.owner.created_by
