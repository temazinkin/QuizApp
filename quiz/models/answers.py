from django.db.models import (
    Model,
    CASCADE,
    CharField,
    BooleanField,
    ForeignKey,
)

from quiz.models import Question


class Answer(Model):
    answer = CharField(
        'ответ',
        max_length=150,
    )
    is_correct = BooleanField(
        'правильный ответ',
        default=False,
    )
    comment = CharField(
        'комментарий к ответу',
        max_length=200,
        blank=True,
    )
    question = ForeignKey(
        Question,
        on_delete=CASCADE,
        verbose_name='вопрос',
    )

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

