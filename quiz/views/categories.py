from django.shortcuts import (
    render,
    get_object_or_404,
)

from quiz.models import (
    Category,
    Quiz,
)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    quizs = Quiz.objects.filter(
        category=category,
        is_public=True,
    ).order_by('npp')

    context = {
        'title': f'Тесты по теме «{category.title}»',
        'category': category,
        'quizs': quizs,
    }

    return render(request, 'quiz/category.html', context=context)
