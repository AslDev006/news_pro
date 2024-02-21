from django.contrib import admin
from .models import *

admin.site.register([Category, Contact])


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'publish_time']
    list_filter = ['publish_time']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['publish_time', 'status']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'create_time', 'active']
    list_filter = ['create_time', 'active']
    search_fields = ['body']
    actions = ['disable_comments', 'activate_comments']
    def disable_comments(self, request, queryset):
        queryset.update(active=False)
    def activate_comments(self, request, queryset):
        queryset.update(active=True)
