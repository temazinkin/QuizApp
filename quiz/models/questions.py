from django.db.models import (
    Model,
    CASCADE,
    CharField,
    TextField,
    ForeignKey,
    ImageField,
)

from quiz.models import Quiz


class Question(Model):
    quiz = ForeignKey(
        Quiz,
        on_delete=CASCADE,
        verbose_name='тест',
    )
    question = CharField(
        'вопрос',
        max_length=150,
    )
    full_text = TextField(
        'описание вопроса',
        blank=True,
    )
    image = ImageField(
        'изображение',
        upload_to='quiz/%Y/',
        blank=True,
    )

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
