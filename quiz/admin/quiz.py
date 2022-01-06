from django.contrib.admin import (
    ModelAdmin,
    register,
)

from adminsortable2.admin import SortableAdminMixin

from quiz.models.quiz import Quiz


@register(Quiz)
class QuizModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
