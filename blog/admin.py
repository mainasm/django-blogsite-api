from django.contrib import admin
from .models import Post, Comment, Category, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)