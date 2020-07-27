
#from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#from project.permissions import IsOwnerOrReadOnly
from project.models import Activity, ActivityMonth, Icon, Calendar,  Owner
from project.serializers import IconSerializer, ActivitySerializer, ActivityMonthSerializer, CalendarSerializer, OwnerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    

class CalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer

    def get_queryset(self):
        return Calendar.objects.filter(owner=self.kwargs['owner_pk'])


class ActivityMonthViewSet(viewsets.ModelViewSet):
    serializer_class = ActivityMonthSerializer
    
    def get_queryset(self):
        return ActivityMonth.objects.filter(
            calendar=self.kwargs['calendar_pk'],
            calendar__owner=self.kwargs['owner_pk']
        )


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(
            calendar=self.kwargs['calendar_pk'],
            calendar__owner=self.kwargs['owner_pk']
        )
    ordering = ('start_time')    

    #def create(self, request, *args, **kwargs):
    #    request.data.calendar_id = kwargs['calendar_pk']
    #    return super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)


class IconViewSet(viewsets.ModelViewSet):
    serializer_class = IconSerializer
    
    def get_queryset(self):
        return Icon.objects.filter(
            calendar=self.kwargs['calendar_pk'],
            calendar__owner=self.kwargs['owner_pk']
        )
    



