from django.conf import settings
from django.db import models


class Question(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', related_name='questions')
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return self.text
        

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question', related_name='answers')
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return self.question.text + ' - ' + self.text


class Vote(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', related_name='votes')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='answer', related_name='vote')