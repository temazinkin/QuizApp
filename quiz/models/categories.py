from django.db.models import (
    Model,
    CharField,
    TextField,
    SlugField,
    PositiveSmallIntegerField,
)
from django.urls import reverse


class Category(Model):
    title = CharField(
        'название',
        max_length=150,
    )
    slug = SlugField(
        'URL',
        unique=True,
    )
    description = TextField(
        'описание',
        blank=True,
    )
    npp = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'category_slug': self.slug,
            }
        )
