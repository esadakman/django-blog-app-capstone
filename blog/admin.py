from django.contrib import admin
from .models import Post, Category,Comment, Like, View
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(View)
