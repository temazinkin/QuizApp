from django.contrib.admin import (
    TabularInline,
)

from quiz.models.answers import Answer


class AnswerTabularInline(TabularInline):
    model = Answer
    min_num = 2
    extra = 0
