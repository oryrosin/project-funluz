from rest_framework import serializers
from multiselectfield import MultiSelectField 
from django.contrib.auth.models import User
from django import forms

from project.models import Activity, AgeGroup, TextMessage, MonthSubtitle


class ActivitySerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Activity
        fields = ['owner','id','start_time', 'duration', 'title', 'content', 'age_group']

class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= AgeGroup
        fields= ['id', 'name']      


class UserSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'activities']

    
class TextMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= TextMessage
        fields= ['id', 'content' ]      


class MonthSubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model= MonthSubtitle
        fields= ['id', 'title' ]      
