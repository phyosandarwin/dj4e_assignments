from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

#  Question has a question and a publication date
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # A Choice has two fields: the text of the choice and a vote tally. 
    # Each Choice is associated with a Question.
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    