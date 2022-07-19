from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Question, Poll


class QuestionDetailView(DetailView):
    model = Question


class QuestionList(ListView):
    model = Question


class PollDetailView(DetailView):
    model = Poll


class PollList(ListView):
    model = Poll