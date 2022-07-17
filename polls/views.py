from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Question


class QuestionDetailView(DetailView):
    model = Question


class QuestionList(ListView):
    model = Question
