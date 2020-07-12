from django.db import models
from django import forms


class AgeGroup(models.Model):
    AGE_GROUP_CHOICES = [
    ("1", "א"), 
    ("2", "ב"), 
    ("3", "ג"), 
    ("4", "ד"), 
    ("5", "ה"),
    ("6", "ו"), 
    ("7", "ז"), 
    ("8", "ח"),
    ("9", "ט"),
]
    agegroup = models.CharField(max_length=1, choices=AGE_GROUP_CHOICES, blank=True, null=True)

class Calendar(models.Model):
    #wtf i put here???
    #client = models.ForeignKey(
    month_in_year = models.DateField() #not sure this is the right way
    is_active = models.BooleanField(default=True)


class Activity(models.Model):
    start_time = models.DateTimeField(help_text='Set starting time', blank=False, null=False)
    end_time = models.DateTimeField(help_text='Set ending time', blank=False, null=False) # Do i validate here or in Views?
    title = models.CharField(max_length=20, default='Peilut', help_text='Set the activity title')
    content = models.TextField(max_length=50, blank=True, default='')
    age_group= models.ManyToManyField(AgeGroup, default= "3")
    #owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE, default= None)
    calendar = models.ForeignKey(Calendar, related_name='activities', on_delete=models.CASCADE, default= None)


class Information(models.Model):
    month_title = models.CharField(max_length=20, help_text='Set the month title')
    content= models.TextField(max_length=200,help_text='Insert general month information', blank=False, default='')
    image = models.ImageField(blank=True, null=True)
    calendar = models.ForeignKey(Calendar, related_name='information', on_delete=models.CASCADE, default= None)
