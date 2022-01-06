from django.contrib.admin import (
    ModelAdmin,
    register,
)

from adminsortable2.admin import SortableAdminMixin

from quiz.models.categories import Category


@register(Category)
class CategoryModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
