from django import template
from django.utils.safestring import mark_safe

from polls.models import Question

register = template.Library()


@register.simple_tag(takes_context=True)
def question(context, id):
    question = Question.objects.get(pk=id)

    choices = question.choice_set.all()
    html = "<p>" + question.question_text +"</p>"
    html += "<p>Варианты ответов</p>"

    for choice in choices:
        html += "<p>" + choice.choice_text + ": " + str(choice.votes) + "</p>"

    return mark_safe(html)
