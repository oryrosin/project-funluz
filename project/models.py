from django.db import models
from django.core.exceptions import ValidationError

class Calendar(models.Model):
    name = models.CharField(max_length=20)


class Month(models.Model):
    month = models.DateField()
    calendar = models.ForeignKey(Calendar, blank=False, null=False ,on_delete=models.CASCADE)


class Information(models.Model):
    month_title = models.CharField(max_length=20, help_text='Set the month title')
    details= models.TextField(max_length=200,help_text='Insert general month information', blank=False, default='')
    bg_image = models.CharField(max_length=40, blank=True, null=True) # way to enter set of backgrounds for use?
    month = models.ForeignKey(Month, blank=False, null=False ,on_delete=models.CASCADE)


class Activity(models.Model):
    start_time = models.DateTimeField(help_text='Set starting time', blank=False, null=False)
    end_time = models.DateTimeField(help_text='Set ending time', blank=False, null=False) 
    title = models.CharField(max_length=20, default='Peilut', help_text='Set the activity title')
    content = models.TextField(max_length=50, blank=True, default='')
    month = models.ForeignKey(Month, blank=False, null=False, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=5, default='ד', help_text='א/ב/ג/ד')

    def clean(self):
        if self.end_time < self.start_time:
            raise ValidationError("End date must be after start date.")



class Icon(models.Model): 
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    z_index = models.IntegerField()
    rotation = models.IntegerField()
    scale = models.FloatField(default=1)
    icon_image = models.CharField(max_length=40, blank=True, null=True) # way to enter set of icons for use?
    month = models.ForeignKey(Month, blank=False, null=False, on_delete=models.CASCADE)
 
