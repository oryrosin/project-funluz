from rest_framework import serializers
from multiselectfield import MultiSelectField 
from django.contrib.auth.models import User
from django import forms

from project.models import Activity, AgeGroup, Calendar, Information

class CalendarSerializer(serializers.ModelSerializer):
    month_in_year = serializers.DateField(input_formats=['%m:%Y'], format='%m:%Y')
    class Meta:
        model= Calendar
        fields= ['id', 'is_active', 'month_in_year']
    

class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= AgeGroup
        fields= ['id', 'agegroup']


class ActivitySerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Activity
        fields = ['id','start_time', 'end_time', 'title', 'content', 'age_group', 'calendar']
  
   
class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Information
        fields= ['id', 'month_title', 'content', 'image', 'calendar' ]      

      
