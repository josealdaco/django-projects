from django.db import models

# Create your models here.


class Question(models.Model):
    """ Question data model"""
    question_date = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """ Choice data model """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
