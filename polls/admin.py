from django.contrib import admin
from .models import Question, Choice, Poll


class PollAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poll, PollAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question", "choice_text", ]


admin.site.register(Choice, ChoiceAdmin)
