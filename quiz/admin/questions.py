from django.contrib.admin import (
    ModelAdmin,
    register,
)

from quiz.models import Question


@register(Question)
class QuestionModelAdmin(ModelAdmin):
    pass
