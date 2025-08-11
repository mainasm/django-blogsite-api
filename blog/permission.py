from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """Existing: allow authors to edit; read-only for others."""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return hasattr(obj, "author") and obj.author == request.user

# Combined permission for Posts: editor OR staff OR author (with special create rule)
class CanManagePost(BasePermission):
    """
    - GET/HEAD/OPTIONS: allow only authenticated users (set via has_permission)
    - POST (create): only editor OR staff
    - PUT/PATCH/DELETE: author OR editor OR staff
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        # safe methods allowed for authenticated users
        if request.method in SAFE_METHODS:
            return True
        # create must be by editor or staff
        if request.method == "POST":
            return request.user.username.lower() in ("editor", "staff")
        # other unsafe methods: allow to proceed to object-level check (so return True here)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # author can edit/delete own object
        if hasattr(obj, "author") and obj.author == request.user:
            return True
        # editors or staff can also manage
        return request.user.username.lower() in ("editor", "staff")

# Combined permission for Comments: moderator OR staff OR author
class CanManageComment(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return request.user.username.lower() in ("moderator", "staff")
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, "author") and obj.author == request.user:
            return True
        return request.user.username.lower() in ("moderator", "staff")

# Combined permission for Categories: alice OR staff OR author
class CanManageCategory(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return request.user.username.lower() in ("alice", "staff")
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, "author") and obj.author == request.user:
            return True
        return request.user.username.lower() in ("alice", "staff")
