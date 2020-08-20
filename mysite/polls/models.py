from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# We'll create two models Questions and Answers
# Finally, note a relationship is defined, using ForeignKey.
# That tells Django each Choice is related to a single Question.
# Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.


class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
