from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('published_date', 'created_date')
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')


admin.site.register(Post, PostAdmin)
