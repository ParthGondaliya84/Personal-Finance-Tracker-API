from django.contrib import admin
from apps.category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "entry_type", "id", "created_by"]


admin.site.register(Category, CategoryAdmin)
