from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)        # 질문 내용
    pub_date = models.DateTimeField('date published')       # 발행 날짜

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)        # 질문 내용(외래키)
    choice_text = models.CharField(max_length=200)                          # 답변 text
    votes = models.IntegerField(default=0)                                  # 득표 수

    def __str__(self):
        return self.choice_text

