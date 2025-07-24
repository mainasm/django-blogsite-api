from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
from .models import Profile

admin.site.register(Profile)
