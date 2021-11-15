from django.conf import settings
from django.db import models


class Question(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', related_name='questions')
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return self.text
        

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question', related_name='options')
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return self.question.text + ' - ' + self.text


class Vote(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', related_name='votes')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, verbose_name='option', related_name='vote')

    def __str__(self):
        return  self.option.question.text + ' - ' + self.option.text + ' - ' + self.owner.email