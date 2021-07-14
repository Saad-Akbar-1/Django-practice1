'''
Models. This is where polls are created.
'''
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''A Question which has many choices.'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return str(self.question_text)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

'''Choice for a Question. Each chice is associated with a question'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return str(self.choice_text)
    
