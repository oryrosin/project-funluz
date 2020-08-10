from rest_framework import serializers
#from django.contrib.auth.models import User

from project.models import Activity, Icon, Information, Month, Calendar


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Information
        fields= ['id', 'month_title', 'details', 'bg_image','Month' ]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','start_time', 'end_time', 'title', 'content', 'age_group', 'month']
        
    def validate(self, attrs):
        instance = Activity(**attrs)
        instance.clean()
        return attrs


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model= Icon
        fields= ['id', 'pos_x', 'pos_y', 'z_index', 'rotation', 'scale', 'icon_image', 'month']


class MonthSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    icons = IconSerializer(many=True, read_only=True)
    informations = InformationSerializer(many=True, read_only=True)

    class Meta:
        model= Month
        fields= ['id', 'month', 'activities', 'icons', 'informations', 'calendar' ]

class CalendarSerializer(serializers.ModelSerializer):
    months = MonthSerializer(many=True, read_only=True)
    class Meta:
        model= Calendar
        fields= ['id', 'name', 'months']