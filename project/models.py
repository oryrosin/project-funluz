from django.db import models
from django import forms

# creatin iterable of coices for age_group 
agegroups=( 
    ("1", "dalet"), 
    ("2", "hey"), 
    ("3", "vav"), 
    ("4", "zain"), 
    ("5", "chet"),
    ("6", "tet"), 
    ("7", "yud"), 
    ("8", "yud-alef"),
    ("9", "yud-bet"),
) 
class AgeGroup(models.Model):
    name= models.CharField(max_length=20)

class Activity(models.Model):
    start_time = models.DateTimeField(help_text='Set starting time')
    duration= models.FloatField(help_text='How many hours will the activity takes? ',default=1.5) 
    title = models.CharField(max_length=20, default='Peilut', help_text='Set the activity title')
    content = models.TextField(max_length=50, blank=True, default='')
    age_group= models.ManyToManyField(AgeGroup)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE, default= None)
    
    def __str__(self):
        return self.title

class TextMessage(models.Model):
    def __init__(self, month):
        self._month = month

    content= models.TextField(max_length=200, blank=False, default='')

    
class MonthSubtitle(models.Model):
    def __init__(self, month):
        self._month = month

    title = models.CharField(max_length=30, blank=True, default='',)

