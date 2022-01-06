from django.db.models import (
    Model,
    PROTECT,
    CharField,
    TextField,
    SlugField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    PositiveSmallIntegerField,
)
from django.urls import reverse

from account.models import Account
from quiz.models import Category


class Quiz(Model):
    author = ForeignKey(
        Account,
        on_delete=PROTECT,
        verbose_name='автор',
    )
    title = CharField(
        'название',
        max_length=150,
    )
    slug = SlugField(
        'URL',
        unique=False,
    )
    description = TextField(
        'описание',
        blank=True,
    )
    is_public = BooleanField(
        'отображается на странице категории',
        default=True,
    )
    category = ForeignKey(
        Category,
        on_delete=PROTECT,
        verbose_name='категория',
    )
    created = DateTimeField(
        'создан',
        auto_now_add=True,
    )
    modified = DateTimeField(
        'изменен',
        auto_now=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quiz'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        unique_together = (
            'slug',
            'category',
        )
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'quiz',
            kwargs={
                'quiz_slug': self.slug,
                'category_slug': self.category.slug,
            }
        )
