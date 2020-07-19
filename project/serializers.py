from rest_framework import serializers
from multiselectfield import MultiSelectField 
#from django.contrib.auth.models import User
from django import forms

from project.models import Activity, Icon, ActivityMonth, Calendar, Client


class ActivityMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model= ActivityMonth
        fields= ['id', 'month_title', 'information', 'bg_image','calendar' ]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','start_time', 'end_time', 'title', 'content', 'age_group', 'calendar']
        
    def time_valid(self):
        if self.start_time > self.end_time:
            raise serializers.ValidationError("end must occur after start")       


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model= Icon
        fields= ['id', 'pos_x', 'pos_y', 'z_index', 'rotation', 'scale', 'icon_image', 'calendar']


class CalendarSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    icons = IconSerializer(many=True, read_only=True)
    activity_month = ActivityMonthSerializer(many=True, read_only=True)

    class Meta:
        model= Calendar
        fields= ['id', 'month', 'activities', 'icons', 'activity_month', 'client' ]

class ClientSerializer(serializers.ModelSerializer):
    calendars = CalendarSerializer(many=True, read_only=True)
    class Meta:
        model= Client
        fields= ['id', 'name', 'calendars']