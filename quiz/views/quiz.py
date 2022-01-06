from django.utils.safestring import SafeString
from django.shortcuts import (
    render,
    get_object_or_404,
)

from config.settings import MEDIA_URL
from quiz.models import Quiz


def quiz_view(request, category_slug, quiz_slug):
    quiz = get_object_or_404(
        Quiz,
        slug=quiz_slug,
        category__slug=category_slug,
    )
    questions = quiz.question_set.all().prefetch_related('answer_set')

    quiz_data = {
        'questions': []
    }

    for question in questions:
        _html = f'{question.question}</h2>'
        _html += f'<div style="margin:-8px 0 20px">' \
                f'<img src="{MEDIA_URL}{question.image}">' \
                f'</div>' if question.image else ''
        _html += f'<p style="margin-top:-8px; line-height:1.4">' \
                f'{question.full_text}' \
                f'</p>' if question.full_text else ''
        _html += '<h2>'

        question_data = {
            'q': _html,
            'a': '',
            'options': [],
        }

        for answer in question.answer_set.all():
            if answer.is_correct:
                question_data['a'] = answer.answer
            question_data['options'].append(answer.answer)

        quiz_data['questions'].append(question_data)

    context = {
        'title': quiz.title,
        'quiz_data': SafeString(quiz_data),
    }

    return render(request, 'quiz/quiz.html', context=context)
