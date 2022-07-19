from django.db import models
from django.urls import reverse


class Poll(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("poll", kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def get_absolute_url(self):
        return reverse("choice", kwargs={'pk': self.id})

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
