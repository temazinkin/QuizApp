from django.contrib.admin import (
    ModelAdmin,
    register,
)

from quiz.admin.answers import AnswerTabularInline
from quiz.models import Question


@register(Question)
class QuestionModelAdmin(ModelAdmin):
    inlines = (
        AnswerTabularInline,
    )
