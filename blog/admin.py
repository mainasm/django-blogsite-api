from django.contrib import admin
from .models import Post, Comment, Category, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


# Existing admin registrations...
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    list_filter = ['user__date_joined']
    search_fields = ['user__username', 'user__email', 'bio']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
