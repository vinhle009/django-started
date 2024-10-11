from django.db import models # type: ignore
import datetime
from django.utils import timezone # type: ignore
from django.contrib import admin
# Create your models here.
#class Question
class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
      return self.question_text
    @admin.display(
            boolean=True,
            ordering='pub_date',
            description='Published recently?',
    )
    def was_published_recently(self):
        return self.pub_date>=timezone.now()- datetime.timedelta(days=1)
#class Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
#class Person
class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
#class Group
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return self.name
#class Membership
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)