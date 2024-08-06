from django.contrib import admin
from .models import *


# admin.site.register(Task)
# admin.site.register(Category)
# admin.site.register(SubTask)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-date',)
    list_per_page = 20

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-deadline',)
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 20



