
#from rest_framework import permissions
#from django.contrib.auth.models import User
from rest_framework import viewsets
#from project.permissions import IsOwnerOrReadOnly
from project.models import Activity, Information, Icon, Month,  Calendar
from project.serializers import IconSerializer, ActivitySerializer, InformationSerializer, MonthSerializer, CalendarSerializer


class CalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()
    

class MonthViewSet(viewsets.ModelViewSet):
    serializer_class = MonthSerializer

    def get_queryset(self):
        return Month.objects.filter(calendar=self.kwargs['calendar_pk'])


class InformationViewSet(viewsets.ModelViewSet):
    serializer_class = InformationSerializer
    
    def get_queryset(self):
        return Information.objects.filter(
            month=self.kwargs['month_pk'],
            month__calendar=self.kwargs['calendar_pk']
        )


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(
            month=self.kwargs['month_pk'],
            month__calendar=self.kwargs['calendar_pk']
        )



class IconViewSet(viewsets.ModelViewSet):
    serializer_class = IconSerializer
    
    def get_queryset(self):
        return Icon.objects.filter(
            month=self.kwargs['month_pk'],
            month__calendar=self.kwargs['calendar_pk']
        )
    



